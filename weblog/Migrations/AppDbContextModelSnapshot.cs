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
                            Title = "Tech"
                        },
                        new
                        {
                            CategoryId = 2,
                            Title = "Politics"
                        },
                        new
                        {
                            CategoryId = 3,
                            Title = "Life"
                        },
                        new
                        {
                            CategoryId = 4,
                            Title = "Science"
                        },
                        new
                        {
                            CategoryId = 5,
                            Title = "Sport"
                        },
                        new
                        {
                            CategoryId = 7,
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(892),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 116, DateTimeKind.Local).AddTicks(3089),
                            ImageUrl = "~/Images/image1.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2791),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2774),
                            ImageUrl = "~/Images/image2.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2872),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2869),
                            ImageUrl = "~/Images/image3.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2896),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2894),
                            ImageUrl = "~/Images/image4.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2919),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2916),
                            ImageUrl = "~/Images/image5.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2944),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2942),
                            ImageUrl = "~/Images/image2.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2966),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2964),
                            ImageUrl = "~/Images/image3.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2988),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2986),
                            ImageUrl = "~/Images/image4.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3010),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3008),
                            ImageUrl = "~/Images/image5.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3033),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3031),
                            ImageUrl = "~/Images/image5.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3055),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3053),
                            ImageUrl = "~/Images/image2.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3076),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3074),
                            ImageUrl = "~/Images/image3.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3212),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3209),
                            ImageUrl = "~/Images/image4.jpg",
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
                            DateChanged = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3236),
                            DatePosted = new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3234),
                            ImageUrl = "~/Images/image5.jpg",
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
