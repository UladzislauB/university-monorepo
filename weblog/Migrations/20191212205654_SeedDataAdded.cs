using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class SeedDataAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<DateTime>(
                name: "DateChanged",
                table: "Posts",
                nullable: false,
                defaultValue: new DateTime(1, 1, 1, 0, 0, 0, 0, DateTimeKind.Unspecified));

            migrationBuilder.AddColumn<bool>(
                name: "InSandbox",
                table: "Posts",
                nullable: false,
                defaultValue: false);

            migrationBuilder.AddColumn<bool>(
                name: "IsLocked",
                table: "Posts",
                nullable: false,
                defaultValue: false);

            migrationBuilder.InsertData(
                table: "Categories",
                columns: new[] { "CategoryId", "Title" },
                values: new object[,]
                {
                    { 1, "Tech" },
                    { 2, "Politics" },
                    { 3, "Life" },
                    { 4, "Science" },
                    { 5, "Sport" },
                    { 7, "Zen" }
                });

            migrationBuilder.InsertData(
                table: "Posts",
                columns: new[] { "PostId", "CategoryId", "DateChanged", "DatePosted", "ImageUrl", "InSandbox", "IsForSubscribersOnly", "IsLocked", "ShortDescription", "Text", "Title" },
                values: new object[,]
                {
                    { 1, 1, new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(5430), new DateTime(2019, 12, 12, 23, 56, 53, 897, DateTimeKind.Local).AddTicks(45), "~/Images/image1.jpg", true, false, false, "Autonomous Driving Updates, HyperAutomation, and More", "", "Here Is A Rundown of 5 Major Tech Trends Hitting 2020" },
                    { 2, 2, new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7526), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7507), "~/Images/image2.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", "Lorem Ipsum" },
                    { 3, 2, new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7607), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7605), "~/Images/image3.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", "Lorem Ipsum" },
                    { 4, 2, new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7629), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7627), "~/Images/image4.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", "Lorem Ipsum" },
                    { 5, 2, new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7651), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7649), "~/Images/image5.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", "Lorem Ipsum" }
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DeleteData(
                table: "Categories",
                keyColumn: "CategoryId",
                keyValue: 3);

            migrationBuilder.DeleteData(
                table: "Categories",
                keyColumn: "CategoryId",
                keyValue: 4);

            migrationBuilder.DeleteData(
                table: "Categories",
                keyColumn: "CategoryId",
                keyValue: 5);

            migrationBuilder.DeleteData(
                table: "Categories",
                keyColumn: "CategoryId",
                keyValue: 7);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5);

            migrationBuilder.DeleteData(
                table: "Categories",
                keyColumn: "CategoryId",
                keyValue: 1);

            migrationBuilder.DeleteData(
                table: "Categories",
                keyColumn: "CategoryId",
                keyValue: 2);

            migrationBuilder.DropColumn(
                name: "DateChanged",
                table: "Posts");

            migrationBuilder.DropColumn(
                name: "InSandbox",
                table: "Posts");

            migrationBuilder.DropColumn(
                name: "IsLocked",
                table: "Posts");
        }
    }
}
