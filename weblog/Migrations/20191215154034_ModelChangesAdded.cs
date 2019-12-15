using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class ModelChangesAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "Claps",
                table: "Posts",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<int>(
                name: "TimeToRead",
                table: "Posts",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<string>(
                name: "ShortDescription",
                table: "Categories",
                nullable: true);

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 18, 40, 34, 137, DateTimeKind.Local).AddTicks(6960), new DateTime(2019, 12, 15, 18, 40, 34, 133, DateTimeKind.Local).AddTicks(9207) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 18, 40, 34, 137, DateTimeKind.Local).AddTicks(9871), new DateTime(2019, 12, 15, 18, 40, 34, 137, DateTimeKind.Local).AddTicks(9841) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 18, 40, 34, 138, DateTimeKind.Local).AddTicks(7), new DateTime(2019, 12, 15, 18, 40, 34, 138, DateTimeKind.Local).AddTicks(1) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 18, 40, 34, 138, DateTimeKind.Local).AddTicks(50), new DateTime(2019, 12, 15, 18, 40, 34, 138, DateTimeKind.Local).AddTicks(46) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 18, 40, 34, 138, DateTimeKind.Local).AddTicks(93), new DateTime(2019, 12, 15, 18, 40, 34, 138, DateTimeKind.Local).AddTicks(89) });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Claps",
                table: "Posts");

            migrationBuilder.DropColumn(
                name: "TimeToRead",
                table: "Posts");

            migrationBuilder.DropColumn(
                name: "ShortDescription",
                table: "Categories");

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(5430), new DateTime(2019, 12, 12, 23, 56, 53, 897, DateTimeKind.Local).AddTicks(45) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7526), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7507) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7607), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7605) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7629), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7627) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7651), new DateTime(2019, 12, 12, 23, 56, 53, 901, DateTimeKind.Local).AddTicks(7649) });
        }
    }
}
