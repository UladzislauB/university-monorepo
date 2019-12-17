using System;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class Initial : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Categories",
                columns: table => new
                {
                    CategoryId = table.Column<int>(nullable: false)
                        .Annotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn),
                    Title = table.Column<string>(nullable: true),
                    ShortDescription = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Categories", x => x.CategoryId);
                });

            migrationBuilder.CreateTable(
                name: "Posts",
                columns: table => new
                {
                    PostId = table.Column<int>(nullable: false)
                        .Annotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn),
                    Title = table.Column<string>(nullable: true),
                    ShortDescription = table.Column<string>(nullable: true),
                    Text = table.Column<string>(nullable: true),
                    ImageUrl = table.Column<string>(nullable: true),
                    DatePosted = table.Column<DateTime>(nullable: false),
                    DateChanged = table.Column<DateTime>(nullable: false),
                    InSandbox = table.Column<bool>(nullable: false),
                    IsLocked = table.Column<bool>(nullable: false),
                    IsForSubscribersOnly = table.Column<bool>(nullable: false),
                    TimeToRead = table.Column<int>(nullable: false),
                    Claps = table.Column<int>(nullable: false),
                    CategoryId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Posts", x => x.PostId);
                    table.ForeignKey(
                        name: "FK_Posts_Categories_CategoryId",
                        column: x => x.CategoryId,
                        principalTable: "Categories",
                        principalColumn: "CategoryId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.InsertData(
                table: "Categories",
                columns: new[] { "CategoryId", "ShortDescription", "Title" },
                values: new object[,]
                {
                    { 1, "Medium's largest active publications about Tech. Follow us to join our community.", "Tech" },
                    { 2, "Medium's largest active publications about Politics. Follow us to join our community.", "Politics" },
                    { 3, "Medium's largest active publications about Life. Follow us to join our community.", "Life" },
                    { 4, "Medium's largest active publications about Science. Follow us to join our community.", "Science" },
                    { 5, "Medium's largest active publications about Sport. Follow us to join our community.", "Sport" },
                    { 7, "Medium's largest active publications about Zen. Follow us to join our community.", "Zen" }
                });

            migrationBuilder.InsertData(
                table: "Posts",
                columns: new[] { "PostId", "CategoryId", "Claps", "DateChanged", "DatePosted", "ImageUrl", "InSandbox", "IsForSubscribersOnly", "IsLocked", "ShortDescription", "Text", "TimeToRead", "Title" },
                values: new object[,]
                {
                    { 1, 1, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(3245), new DateTime(2019, 12, 17, 11, 44, 18, 455, DateTimeKind.Local).AddTicks(6282), "https://localhost:5001/Images/image1.jpg", true, false, false, "Autonomous Driving Updates, HyperAutomation, and More", "", 0, "Here Is A Rundown of 5 Major Tech Trends Hitting 2020" },
                    { 6, 1, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5252), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5250), "https://source.unsplash.com/random/800x505", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 7, 1, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5274), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5272), "https://source.unsplash.com/random/800x500", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 8, 1, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5296), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5294), "https://source.unsplash.com/random/800x507", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 9, 1, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5317), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5315), "https://source.unsplash.com/random/800x508", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 2, 2, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5102), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5083), "https://source.unsplash.com/random/800x501", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 3, 2, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5178), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5175), "https://source.unsplash.com/random/800x502", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 4, 2, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5202), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5200), "https://source.unsplash.com/random/800x503", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 5, 2, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5225), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5223), "https://source.unsplash.com/random/800x504", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 10, 3, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5341), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5338), "https://source.unsplash.com/random/800x510", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 11, 3, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5362), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5360), "https://source.unsplash.com/random/800x511", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 12, 3, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5383), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5381), "https://source.unsplash.com/random/800x512", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 13, 3, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5404), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5402), "https://source.unsplash.com/random/800x513", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 14, 3, 0, new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5483), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5481), "https://source.unsplash.com/random/800x514", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" }
                });

            migrationBuilder.CreateIndex(
                name: "IX_Posts_CategoryId",
                table: "Posts",
                column: "CategoryId");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Posts");

            migrationBuilder.DropTable(
                name: "Categories");
        }
    }
}
