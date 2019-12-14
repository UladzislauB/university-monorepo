using System;

namespace weblog.Models
{
    public class Post
    {
        public int PostId { get; set; }
        public string Title { get; set; }
        public string ShortDescription { get; set; }
        public string Text { get; set; }
        public string ImageUrl { get; set; }
        public DateTime DatePosted { get; set; }
        public DateTime DateChanged { get; set; }
        public bool InSandbox { get; set; }
        public bool IsLocked { get; set; }
        public bool IsForSubscribersOnly { get; set; }
        public int CategoryId { get; set; }
        public Category Category { get; set; }
    }
}