using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using weblog.Models;
using weblog.ViewModels;
using System.Threading.Tasks;
using System.Web;
using Microsoft.AspNetCore.Authorization;
using Microsoft.Extensions.Logging;
using weblog.Logging;


namespace weblog.Controllers
{
    public class PostController : Controller
    {
        private readonly IPostRepository _postRepository;
        private readonly ICategoryRepository _categoryRepository;
        private readonly ICommentRepository _commentRepository;
        private readonly ILogger _logger;
        
        
        public PostController(ICategoryRepository categoryRepository, IPostRepository postRepository,
            ICommentRepository commentRepository, ILogger<PostController> logger)
        {
            _categoryRepository = categoryRepository;
            _postRepository = postRepository;
            _commentRepository = commentRepository;
            _logger = logger;
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
                ViewData["category"] = "";
            }
            else
            {
                posts = _postRepository.AllPosts.Where(p => p.Category.Title == category)
                    .OrderByDescending(p => p.DatePosted);
                currentCategory = _categoryRepository.AllCategories.FirstOrDefault(c => c.Title == category)?.Title;
                ViewData["category"] = currentCategory;
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
            _logger.LogInformation(LoggingEvents.GetItem, "Getting detail {Id}", id);
            if (post == null)
            {
                _logger.LogWarning(LoggingEvents.GetItemNotFound, "Detail({Id}) NOT FOUND", id);
                return NotFound();
            }
                
            post.Category = _categoryRepository.AllCategories.FirstOrDefault(c =>
                                       c.CategoryId == post.CategoryId);
            ViewData["category"] = post.Category?.Title;
            var comments = _commentRepository.AllComments.
                Where(com => com.PostId == id).OrderByDescending(com => com.CommentId);
            return View(new PostDetailViewModel
            {
                Post = post,
                Comments = comments
            });
        }
    }
}