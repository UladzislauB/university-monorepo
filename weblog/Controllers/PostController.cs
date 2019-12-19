using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using weblog.Models;
using weblog.ViewModels;
using System.Threading.Tasks;
using System.Web;


namespace weblog.Controllers
{
    public class PostController : Controller
    {
        private readonly IPostRepository _postRepository;
        private readonly ICategoryRepository _categoryRepository;
        private readonly ICommentRepository _commentRepository;
        private readonly AppDbContext _appDbContext;
        
        public PostController(ICategoryRepository categoryRepository, IPostRepository postRepository,
            ICommentRepository commentRepository, AppDbContext appDbContext)
        {
            _categoryRepository = categoryRepository;
            _postRepository = postRepository;
            _commentRepository = commentRepository;
            _appDbContext = appDbContext;
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
            ViewData["category"] = "";
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