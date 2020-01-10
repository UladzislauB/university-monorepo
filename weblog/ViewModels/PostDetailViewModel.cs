using System.Collections.Generic;
using weblog.Models;

namespace weblog.ViewModels
{
    public class PostDetailViewModel
    {
        public Post Post { get; set; }
        
        public IEnumerable<Comment> Comments { get; set; }
    }
}