using System;
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

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            
            //seed categories
            modelBuilder.Entity<Category>().HasData(new Category {CategoryId = 1, Title = "Tech"});
            modelBuilder.Entity<Category>().HasData(new Category {CategoryId = 2, Title = "Politics"});
            modelBuilder.Entity<Category>().HasData(new Category {CategoryId = 3, Title = "Life"});
            modelBuilder.Entity<Category>().HasData(new Category {CategoryId = 4, Title = "Science"});
            modelBuilder.Entity<Category>().HasData(new Category {CategoryId = 5, Title = "Sport"});
            modelBuilder.Entity<Category>().HasData(new Category {CategoryId = 7, Title = "Zen"});
            
            
            //seed posts
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 1,
                Title = "Here Is A Rundown of 5 Major Tech Trends Hitting 2020",
                ShortDescription = "Autonomous Driving Updates, HyperAutomation, and More",
                Text = "",
                ImageUrl = "~/Images/image1.jpg",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 1
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 2,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x501",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 2
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 3,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x502",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 2
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 4,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x503",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 2
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 5,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x504",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 2
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 6,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x505",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 1
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 7,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x500",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 1
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 8,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x507",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 1
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 9,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x508",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 1
            });
             modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 10,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x510",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 3
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 11,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x511",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 3
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 12,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x512",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 3
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 13,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x513",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 3
            });
            modelBuilder.Entity<Post>().HasData(new Post
            {
                PostId = 14,
                Title = "Lorem Ipsum",
                ShortDescription = "Lorem ipsum dolor sit amet",
                Text = "",
                ImageUrl = "https://source.unsplash.com/random/800x514",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 3
            });
        }
    }
}