using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using weblog.Models;
using weblog.Services;
using weblog.ViewModels;

namespace weblog.Controllers
{
    public class HomeController : Controller
    {
        private readonly IPostRepository _postRepository;
        private readonly EmailService _emailService;

        public HomeController(IPostRepository postRepository, EmailService emailService)
        {
            _postRepository = postRepository;
            _emailService = emailService;
        }
        
        
        public async Task<IActionResult> SendMessage()
        {
            await _emailService.SendEmailAsync("vasilyuk.vlad.kbr@yandex.by", "Тема письма", "Текст письма: текст!");
            return RedirectToAction("Index");
        }
        
        // GET
        public IActionResult Index()
        {
            var homeViewModel = new HomeViewModel
            {
                FirstCategoryPosts = _postRepository.AllPosts.Where(p => p.CategoryId == 1).ToList(),
                SecondCategoryPosts = _postRepository.AllPosts,
                ThirdCategoryPosts = _postRepository.AllPosts.Where(p => p.CategoryId == 3),
            };
            return View(homeViewModel);
        }
    }
}