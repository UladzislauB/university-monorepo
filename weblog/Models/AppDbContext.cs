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
                ImageUrl = "~/Images/image2.jpg",
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
                ImageUrl = "~/Images/image3.jpg",
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
                ImageUrl = "~/Images/image4.jpg",
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
                ImageUrl = "~/Images/image5.jpg",
                DatePosted = DateTime.Now,
                DateChanged = DateTime.Now,
                InSandbox = true,
                IsLocked = false,
                IsForSubscribersOnly = false,
                CategoryId = 2
            });
        }
    }
}