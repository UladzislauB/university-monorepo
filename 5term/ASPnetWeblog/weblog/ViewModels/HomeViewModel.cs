using System.Collections.Generic;
using weblog.Models;

namespace weblog.ViewModels
{
    public class HomeViewModel
    {
        public List<Post> FirstCategoryPosts;
        public IEnumerable<Post> SecondCategoryPosts;
        public IEnumerable<Post> ThirdCategoryPosts;
    }
}