using System.Collections.Generic;
using System.Linq;

namespace weblog.Models
{
    public interface IPostRepository
    {
        IEnumerable<Post> AllPosts { get; }
        Post GetPostById(int postId);

    }
}