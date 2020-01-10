using System;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class CommentModelAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Comments",
                columns: table => new
                {
                    CommentId = table.Column<int>(nullable: false)
                        .Annotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn),
                    Name = table.Column<string>(nullable: true),
                    Body = table.Column<string>(nullable: true),
                    PostId = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Comments", x => x.CommentId);
                });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(4634), new DateTime(2019, 12, 19, 12, 26, 53, 642, DateTimeKind.Local).AddTicks(7319) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6493), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6469) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6577), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6574) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6601), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6599) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6624), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6621) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 6,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6650), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6648) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 7,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6672), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6670) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 8,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6694), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6692) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 9,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6716), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6714) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 10,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6740), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6738) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 11,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6762), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6759) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 12,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6783), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6781) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 13,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6805), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6803) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 14,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6826), new DateTime(2019, 12, 19, 12, 26, 53, 646, DateTimeKind.Local).AddTicks(6824) });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Comments");

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(3245), new DateTime(2019, 12, 17, 11, 44, 18, 455, DateTimeKind.Local).AddTicks(6282) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5102), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5083) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5178), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5175) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5202), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5200) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5225), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5223) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 6,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5252), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5250) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 7,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5274), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5272) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 8,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5296), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5294) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 9,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5317), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5315) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 10,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5341), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5338) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 11,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5362), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5360) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 12,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5383), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5381) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 13,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5404), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5402) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 14,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5483), new DateTime(2019, 12, 17, 11, 44, 18, 459, DateTimeKind.Local).AddTicks(5481) });
        }
    }
}
