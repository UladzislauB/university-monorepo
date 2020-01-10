using System.Collections.Generic;

namespace weblog.Models
{
    public interface ICommentRepository
    {
        IEnumerable<Comment> AllComments { get; }
    }
}