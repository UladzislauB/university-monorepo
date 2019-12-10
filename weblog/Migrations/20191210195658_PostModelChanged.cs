using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class PostModelChanged : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<DateTime>(
                name: "DatePosted",
                table: "Posts",
                nullable: false,
                defaultValue: new DateTime(1, 1, 1, 0, 0, 0, 0, DateTimeKind.Unspecified));

            migrationBuilder.AddColumn<bool>(
                name: "IsForSubscribersOnly",
                table: "Posts",
                nullable: false,
                defaultValue: false);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "DatePosted",
                table: "Posts");

            migrationBuilder.DropColumn(
                name: "IsForSubscribersOnly",
                table: "Posts");
        }
    }
}
