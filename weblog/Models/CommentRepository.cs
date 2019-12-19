using System.Collections.Generic;

namespace weblog.Models
{
    public class CommentRepository: ICommentRepository
    {
        private readonly AppDbContext _appDbContext;

        public CommentRepository(AppDbContext appDbContext)
        {
            _appDbContext = appDbContext;
        }

        public IEnumerable<Comment> AllComments => _appDbContext.Comments;
    }
}