#include <boost/multiprecision/cpp_int.hpp>

#include <chrono>
#include <ratio>
#include <thread>
#include <atomic>
#include <vector>
#include <random>
#include <utility>

using uint1024 = boost::multiprecision::number<boost::multiprecision::cpp_int_backend<4096, 4096, 
    boost::multiprecision::signed_magnitude, boost::multiprecision::unchecked, void>>;

struct TRSAKeys {
    std::pair<uint1024, uint1024> PublicKey;
    std::pair<uint1024, uint1024> PrivateKey;

    TRSAKeys(uint1024 openKey, uint1024 privateKey, uint1024 module)
        : PublicKey{openKey, module}
        , PrivateKey{privateKey, module}
    {}
};

uint1024 BinPower(const uint1024& base, uint1024 power, const uint1024& mod) {
    if (power == 0) {
        return 1;
    } else {
        auto value = BinPower(base, power / 2, mod);
        value = (value * value) % mod;

        if (power % 2 != 0) {
            value = (value * base) % mod;
        } 

        return value;
    }
}


template<class Function>
void TestPerfomance(Function function) {
    auto start = std::chrono::high_resolution_clock::now();
    function();
    auto finish = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> time_ms = finish - start;
    std::cout << "function took: " << std::fixed << time_ms.count() << " ms" << std::endl;
}


namespace {
    void PrintKeys(const TRSAKeys& rsaKeys) {
        std::cout << "Public key:\n" << rsaKeys.PublicKey.first << "\n" << rsaKeys.PublicKey.second;
        std::cout << std::endl;
        std::cout << "Private key:\n" << rsaKeys.PrivateKey.first << "\n" << rsaKeys.PrivateKey.second;
        std::cout << std::endl;
    }
}

namespace {
    // Miller–Rabin primality test
    bool IsPrime(uint1024 value) {
        constexpr static std::array<uint32_t, 10> primes = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
        const static uint1024 temp{1};

        for (auto p : primes) {
            if (value % p == 0) {
                return false;
            }
        }

        const uint1024 base = 2;
        --value;
        uint32_t power = 0;
        while((value & (temp << power)) == 0) {
            ++power;
        }
        ++value;
        uint1024 q{value / (temp << power)};

        // std::cout << power << " " << q << std::endl;
        // std::cout << BinPower(base, q, value) << std::endl;

        auto surplus = BinPower(base, q, value);
        if (surplus == 1 || surplus == value - 1) {
            return true;
        }
		
        for (uint32_t i = 1; i < power; ++i) {
            surplus = (surplus * surplus) % value;
            if (surplus == value - 1) {
                return true;
            }
        }

        return false;
    }

    uint1024 GetRandBits(int bits, std::default_random_engine* engine) {
        std::uniform_int_distribution<int> uniform_dist(0, 1);
    
        uint1024 value = 0;
        for (int i = 0; i < bits; ++i) {
            if ((uniform_dist(*engine) & 1) == 0) {
                value |= (uint1024{1} << i);
            } 
        }

        return value;
    }

    uint1024 FPrime(int32_t bits) {
        std::random_device r;
        std::default_random_engine engine(r());

        uint1024 e = BinPower(2, 16, 1000000000) + 1;
        uint1024 mask = (uint1024{3} << (bits - 2)) | 1;
        int count = 0;
        while (true) {
            ++count;
            auto value = GetRandBits(bits, &engine) | mask;
            if (value % e != 1 && IsPrime(value)) {
                // std::cout << "Iterations: " << count << std::endl;
                // std::cout << "Prime: " << value << std::endl;
                return value;
            }
        }
    }
    
}


uint1024 GeneratePrime(uint32_t bitsCount) {
    return FPrime(bitsCount);
}


uint1024 TransformFromBits(const std::string& bits, int bitsCount) {
    if (bitsCount != bits.length()) {
        std::cerr << "Warning. Incorrect sizes\n";
    }

    uint1024 value = 0;
    for (int i = 0, j = bits.length() - 1; j >= 0 && i < bitsCount; --j, ++i) {
        if (bits[j] == '0') {
            continue;
        }

        value += uint1024{1} << i;
    }

    return value;
}

std::string TransformToBits(const std::string& value_p, int bitsCount) {
    uint1024 value{value_p};

    std::string bits;
    for (int i = bitsCount - 1; i >= 0; --i) {
        if (value & (uint1024{1} << i)) {
            bits += '1';
        } else {
            bits += '0';
        }
    }

    return bits;
}

namespace {
    std::pair<uint1024, uint1024> ExtendedEuclidian(const uint1024& e, const uint1024& phi) {
        // e * (x) + phi * (y) = gcd(e, phi) = 1;  find(x)
        if (e == 0) {
            return std::make_pair(0, 1);
        }

        auto [x1, y1] = ExtendedEuclidian(phi % e, e);
        return std::make_pair(y1 - (phi / e) * x1 ,x1);
    }
}


TRSAKeys GenerateRSAKeys(const uint1024& p, const uint1024& q, int bitsCount) {
    uint1024 moduleValue = p * q;
    uint1024 phi = (p - 1) * (q - 1);

    uint1024 openExp;
    uint1024 privateExp = -1;

    while (privateExp < 0) {
        openExp = GeneratePrime(std::min(bitsCount, 32));
        auto [privateExpValue, temp] = ExtendedEuclidian(openExp, phi);
        privateExp = std::move(privateExpValue);
    }

    if ((openExp * privateExp) % phi != 1) {
        std::cerr << "Warning. Incorrect exps\n";
    }

    // std::cout << "rsa keys\n";
    // std::cout << "n: " << moduleValue << "\nphi: " << phi << "\ne: " << openExp << std::endl;
    // std::cout << "privateExp: " << privateExp << std::endl;

    return TRSAKeys{openExp, privateExp, moduleValue};
}


uint1024 Encode(uint1024 value, const std::pair<uint1024, uint1024>& publicKey) {
    if (value >= publicKey.second) {
        std::cerr << "Block is too large.\n";
    }

    return BinPower(value, publicKey.first, publicKey.second);
}

uint1024 Decode(uint1024 value, const std::pair<uint1024, uint1024>& privateKey) {
    return BinPower(value, privateKey.first, privateKey.second);
}


int main() {
    constexpr int bitsCount = 1024;

    auto p = GeneratePrime(bitsCount);
    auto q = GeneratePrime(bitsCount);
    
    auto rsaKeys = GenerateRSAKeys(p, q, bitsCount);
    PrintKeys(rsaKeys);

    uint1024 value{"1230948092384098"};
    auto encrypted = Encode(value, rsaKeys.PublicKey);
    auto decrypted = Decode(encrypted, rsaKeys.PrivateKey);
    std::cout << "\nMessage: " << value << std::endl;
    std::cout << "Encrypted: " << encrypted << std::endl;
    std::cout << "Decrypted: " << decrypted << std::endl;
    std::cout << "======================================================\n";

    return 0;
}
