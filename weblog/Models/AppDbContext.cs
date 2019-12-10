using Microsoft.EntityFrameworkCore;

namespace weblog.Models
{
    public class AppDbContext: DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options): base(options)
        {
            
        }
        
        public DbSet<Post> Posts { get; set; }
        public DbSet<Category> Categories { get; set; }
    }
}