using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class MoreSeedPostsAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(892), new DateTime(2019, 12, 15, 19, 2, 38, 116, DateTimeKind.Local).AddTicks(3089) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2791), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2774) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2872), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2869) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2896), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2894) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2919), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2916) });

            migrationBuilder.InsertData(
                table: "Posts",
                columns: new[] { "PostId", "CategoryId", "Claps", "DateChanged", "DatePosted", "ImageUrl", "InSandbox", "IsForSubscribersOnly", "IsLocked", "ShortDescription", "Text", "TimeToRead", "Title" },
                values: new object[,]
                {
                    { 6, 1, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2944), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2942), "~/Images/image2.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 7, 1, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2966), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2964), "~/Images/image3.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 8, 1, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2988), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(2986), "~/Images/image4.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 9, 1, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3010), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3008), "~/Images/image5.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 10, 3, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3033), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3031), "~/Images/image5.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 11, 3, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3055), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3053), "~/Images/image2.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 12, 3, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3076), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3074), "~/Images/image3.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 13, 3, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3212), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3209), "~/Images/image4.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" },
                    { 14, 3, 0, new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3236), new DateTime(2019, 12, 15, 19, 2, 38, 120, DateTimeKind.Local).AddTicks(3234), "~/Images/image5.jpg", true, false, false, "Lorem ipsum dolor sit amet", "", 0, "Lorem Ipsum" }
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 6);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 7);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 8);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 9);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 10);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 11);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 12);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 13);

            migrationBuilder.DeleteData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 14);

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
    }
}
