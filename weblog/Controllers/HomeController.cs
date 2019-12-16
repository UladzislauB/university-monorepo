using System.Linq;
using Microsoft.AspNetCore.Mvc;
using weblog.Models;
using weblog.ViewModels;

namespace weblog.Controllers
{
    public class HomeController : Controller
    {
        private readonly IPostRepository _postRepository;

        public HomeController(IPostRepository postRepository)
        {
            _postRepository = postRepository;
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