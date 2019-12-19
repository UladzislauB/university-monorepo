using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class CommentDateAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Date",
                table: "Comments",
                nullable: true);

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(2244), new DateTime(2019, 12, 19, 23, 58, 9, 792, DateTimeKind.Local).AddTicks(6025) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4097), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4077) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4180), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4178) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4204), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4201) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4226), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4224) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 6,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4252), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4250) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 7,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4273), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4271) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 8,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4295), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4292) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 9,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4316), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4314) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 10,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4339), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4337) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 11,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4360), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4358) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 12,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4381), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4379) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 13,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4401), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4399) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 14,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4422), new DateTime(2019, 12, 19, 23, 58, 9, 796, DateTimeKind.Local).AddTicks(4420) });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Date",
                table: "Comments");

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
    }
}
