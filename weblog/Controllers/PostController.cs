using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using weblog.Models;
using weblog.ViewModels;

namespace weblog.Controllers
{
    public class PostController : Controller
    {
        private readonly IPostRepository _postRepository;
        private readonly ICategoryRepository _categoryRepository;

        public PostController(ICategoryRepository categoryRepository, IPostRepository postRepository)
        {
            _categoryRepository = categoryRepository;
            _postRepository = postRepository;
        }
        
        
        // GET
        public ViewResult List(string category)
        {
            IEnumerable<Post> posts;
            string currentCategory;
            if (string.IsNullOrEmpty(category))
            {
                posts = _postRepository.AllPosts.OrderByDescending(p => p.DatePosted);
                currentCategory = "All post";
            }
            else
            {
                posts = _postRepository.AllPosts.Where(p => p.Category.Title == category)
                    .OrderByDescending(p => p.DatePosted);
                currentCategory = _categoryRepository.AllCategories.FirstOrDefault(c => c.Title == category)?.Title;
            }
            return View(new PostListViewModel
            {
                Posts = posts,
                CurrentCategory = currentCategory
            });
        }

        public IActionResult Detail(int id)
        {
            var post = _postRepository.GetPostById(id);
            if (post == null)
                return NotFound();
            return View(post);
        }
    }
}