using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;

namespace weblog.Models
{
    public class PostRepository: IPostRepository
    {
        private readonly AppDbContext _appDbContext;

        public PostRepository(AppDbContext appDbContext)
        {
            _appDbContext = appDbContext;
        }

        public IEnumerable<Post> AllPosts => _appDbContext.Posts.Include(c => c.Category);


        public Post GetPostById(int postId) => _appDbContext.Posts.FirstOrDefault(p => p.PostId == postId);
    }
}