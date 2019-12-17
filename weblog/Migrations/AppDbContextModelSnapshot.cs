﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using weblog.Models;

namespace weblog.Migrations
{
    [DbContext(typeof(AppDbContext))]
    partial class AppDbContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "3.1.0")
                .HasAnnotation("Relational:MaxIdentifierLength", 64);

            modelBuilder.Entity("weblog.Models.Category", b =>
                {
                    b.Property<int>("CategoryId")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<string>("ShortDescription")
                        .HasColumnType("longtext CHARACTER SET utf8mb4");

                    b.Property<string>("Title")
                        .HasColumnType("longtext CHARACTER SET utf8mb4");

                    b.HasKey("CategoryId");

                    b.ToTable("Categories");

                    b.HasData(
                        new
                        {
                            CategoryId = 1,
                            ShortDescription = "Medium's largest active publications about Tech. Follow us to join our community.",
                            Title = "Tech"
                        },
                        new
                        {
                            CategoryId = 2,
                            ShortDescription = "Medium's largest active publications about Politics. Follow us to join our community.",
                            Title = "Politics"
                        },
                        new
                        {
                            CategoryId = 3,
                            ShortDescription = "Medium's largest active publications about Life. Follow us to join our community.",
                            Title = "Life"
                        },
                        new
                        {
                            CategoryId = 4,
                            ShortDescription = "Medium's largest active publications about Science. Follow us to join our community.",
                            Title = "Science"
                        },
                        new
                        {
                            CategoryId = 5,
                            ShortDescription = "Medium's largest active publications about Sport. Follow us to join our community.",
                            Title = "Sport"
                        },
                        new
                        {
                            CategoryId = 7,
                            ShortDescription = "Medium's largest active publications about Zen. Follow us to join our community.",
                            Title = "Zen"
                        });
                });

            modelBuilder.Entity("weblog.Models.Post", b =>
                {
                    b.Property<int>("PostId")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    b.Property<int>("CategoryId")
                        .HasColumnType("int");

                    b.Property<int>("Claps")
                        .HasColumnType("int");

                    b.Property<DateTime>("DateChanged")
                        .HasColumnType("datetime(6)");

                    b.Property<DateTime>("DatePosted")
                        .HasColumnType("datetime(6)");

                    b.Property<string>("ImageUrl")
                        .HasColumnType("longtext CHARACTER SET utf8mb4");

                    b.Property<bool>("InSandbox")
                        .HasColumnType("tinyint(1)");

                    b.Property<bool>("IsForSubscribersOnly")
                        .HasColumnType("tinyint(1)");

                    b.Property<bool>("IsLocked")
                        .HasColumnType("tinyint(1)");

                    b.Property<string>("ShortDescription")
                        .HasColumnType("longtext CHARACTER SET utf8mb4");

                    b.Property<string>("Text")
                        .HasColumnType("longtext CHARACTER SET utf8mb4");

                    b.Property<int>("TimeToRead")
                        .HasColumnType("int");

                    b.Property<string>("Title")
                        .HasColumnType("longtext CHARACTER SET utf8mb4");

                    b.HasKey("PostId");

                    b.HasIndex("CategoryId");

                    b.ToTable("Posts");

                    b.HasData(
                        new
                        {
                            PostId = 1,
                            CategoryId = 1,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(3245),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 455, DateTimeKind.Local).AddTicks(6282),
                            ImageUrl = "https://localhost:5001/Images/image1.jpg",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Autonomous Driving Updates, HyperAutomation, and More",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Here Is A Rundown of 5 Major Tech Trends Hitting 2020"
                        },
                        new
                        {
                            PostId = 2,
                            CategoryId = 2,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5102),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5083),
                            ImageUrl = "https://source.unsplash.com/random/800x501",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 3,
                            CategoryId = 2,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5178),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5175),
                            ImageUrl = "https://source.unsplash.com/random/800x502",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 4,
                            CategoryId = 2,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5202),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5200),
                            ImageUrl = "https://source.unsplash.com/random/800x503",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 5,
                            CategoryId = 2,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5225),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5223),
                            ImageUrl = "https://source.unsplash.com/random/800x504",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 6,
                            CategoryId = 1,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5252),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5250),
                            ImageUrl = "https://source.unsplash.com/random/800x505",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 7,
                            CategoryId = 1,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5274),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5272),
                            ImageUrl = "https://source.unsplash.com/random/800x500",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 8,
                            CategoryId = 1,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5296),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5294),
                            ImageUrl = "https://source.unsplash.com/random/800x507",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 9,
                            CategoryId = 1,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5317),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5315),
                            ImageUrl = "https://source.unsplash.com/random/800x508",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 10,
                            CategoryId = 3,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5341),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5338),
                            ImageUrl = "https://source.unsplash.com/random/800x510",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 11,
                            CategoryId = 3,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5362),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5360),
                            ImageUrl = "https://source.unsplash.com/random/800x511",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 12,
                            CategoryId = 3,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5383),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5381),
                            ImageUrl = "https://source.unsplash.com/random/800x512",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 13,
                            CategoryId = 3,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5404),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5402),
                            ImageUrl = "https://source.unsplash.com/random/800x513",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        },
                        new
                        {
                            PostId = 14,
                            CategoryId = 3,
                            Claps = 0,
                            DateChanged = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5483),
                            DatePosted = new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5481),
                            ImageUrl = "https://source.unsplash.com/random/800x514",
                            InSandbox = true,
                            IsForSubscribersOnly = false,
                            IsLocked = false,
                            ShortDescription = "Lorem ipsum dolor sit amet",
                            Text = "",
                            TimeToRead = 0,
                            Title = "Lorem Ipsum"
                        });
                });

            modelBuilder.Entity("weblog.Models.Post", b =>
                {
                    b.HasOne("weblog.Models.Category", "Category")
                        .WithMany("Posts")
                        .HasForeignKey("CategoryId")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });
#pragma warning restore 612, 618
        }
    }
}
