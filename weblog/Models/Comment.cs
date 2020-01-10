using System.ComponentModel.DataAnnotations.Schema;

namespace weblog.Models
{
    public class Comment
    {
        public int CommentId { get; set; }
        
        public string Name { get; set; }
        
        public string Body { get; set; }
        
        public int PostId { get; set; }
        
        public string Date { get; set; }
    }
}