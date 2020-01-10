using System;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;

namespace weblog.Migrations
{
    public partial class IdentityAdded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "AspNetRoles",
                columns: table => new
                {
                    Id = table.Column<string>(nullable: false),
                    Name = table.Column<string>(maxLength: 256, nullable: true),
                    NormalizedName = table.Column<string>(maxLength: 256, nullable: true),
                    ConcurrencyStamp = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetRoles", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "AspNetUsers",
                columns: table => new
                {
                    Id = table.Column<string>(nullable: false),
                    UserName = table.Column<string>(maxLength: 256, nullable: true),
                    NormalizedUserName = table.Column<string>(maxLength: 256, nullable: true),
                    Email = table.Column<string>(maxLength: 256, nullable: true),
                    NormalizedEmail = table.Column<string>(maxLength: 256, nullable: true),
                    EmailConfirmed = table.Column<bool>(nullable: false),
                    PasswordHash = table.Column<string>(nullable: true),
                    SecurityStamp = table.Column<string>(nullable: true),
                    ConcurrencyStamp = table.Column<string>(nullable: true),
                    PhoneNumber = table.Column<string>(nullable: true),
                    PhoneNumberConfirmed = table.Column<bool>(nullable: false),
                    TwoFactorEnabled = table.Column<bool>(nullable: false),
                    LockoutEnd = table.Column<DateTimeOffset>(nullable: true),
                    LockoutEnabled = table.Column<bool>(nullable: false),
                    AccessFailedCount = table.Column<int>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetUsers", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "AspNetRoleClaims",
                columns: table => new
                {
                    Id = table.Column<int>(nullable: false)
                        .Annotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn),
                    RoleId = table.Column<string>(nullable: false),
                    ClaimType = table.Column<string>(nullable: true),
                    ClaimValue = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetRoleClaims", x => x.Id);
                    table.ForeignKey(
                        name: "FK_AspNetRoleClaims_AspNetRoles_RoleId",
                        column: x => x.RoleId,
                        principalTable: "AspNetRoles",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "AspNetUserClaims",
                columns: table => new
                {
                    Id = table.Column<int>(nullable: false)
                        .Annotation("MySql:ValueGenerationStrategy", MySqlValueGenerationStrategy.IdentityColumn),
                    UserId = table.Column<string>(nullable: false),
                    ClaimType = table.Column<string>(nullable: true),
                    ClaimValue = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetUserClaims", x => x.Id);
                    table.ForeignKey(
                        name: "FK_AspNetUserClaims_AspNetUsers_UserId",
                        column: x => x.UserId,
                        principalTable: "AspNetUsers",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "AspNetUserLogins",
                columns: table => new
                {
                    LoginProvider = table.Column<string>(maxLength: 128, nullable: false),
                    ProviderKey = table.Column<string>(maxLength: 128, nullable: false),
                    ProviderDisplayName = table.Column<string>(nullable: true),
                    UserId = table.Column<string>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetUserLogins", x => new { x.LoginProvider, x.ProviderKey });
                    table.ForeignKey(
                        name: "FK_AspNetUserLogins_AspNetUsers_UserId",
                        column: x => x.UserId,
                        principalTable: "AspNetUsers",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "AspNetUserRoles",
                columns: table => new
                {
                    UserId = table.Column<string>(nullable: false),
                    RoleId = table.Column<string>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetUserRoles", x => new { x.UserId, x.RoleId });
                    table.ForeignKey(
                        name: "FK_AspNetUserRoles_AspNetRoles_RoleId",
                        column: x => x.RoleId,
                        principalTable: "AspNetRoles",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_AspNetUserRoles_AspNetUsers_UserId",
                        column: x => x.UserId,
                        principalTable: "AspNetUsers",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "AspNetUserTokens",
                columns: table => new
                {
                    UserId = table.Column<string>(nullable: false),
                    LoginProvider = table.Column<string>(maxLength: 128, nullable: false),
                    Name = table.Column<string>(maxLength: 128, nullable: false),
                    Value = table.Column<string>(nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AspNetUserTokens", x => new { x.UserId, x.LoginProvider, x.Name });
                    table.ForeignKey(
                        name: "FK_AspNetUserTokens_AspNetUsers_UserId",
                        column: x => x.UserId,
                        principalTable: "AspNetUsers",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 1,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(6419), new DateTime(2019, 12, 20, 14, 7, 21, 271, DateTimeKind.Local).AddTicks(9246) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 2,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(8810), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(8791) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 3,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(8897), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(8894) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 4,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9016), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9013) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 5,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9046), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9044) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 6,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9076), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9074) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 7,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9098), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9096) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 8,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9121), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9119) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 9,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9143), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9141) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 10,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9168), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9166) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 11,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9190), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9188) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 12,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9212), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9210) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 13,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9234), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9232) });

            migrationBuilder.UpdateData(
                table: "Posts",
                keyColumn: "PostId",
                keyValue: 14,
                columns: new[] { "DateChanged", "DatePosted" },
                values: new object[] { new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9256), new DateTime(2019, 12, 20, 14, 7, 21, 275, DateTimeKind.Local).AddTicks(9254) });

            migrationBuilder.CreateIndex(
                name: "IX_AspNetRoleClaims_RoleId",
                table: "AspNetRoleClaims",
                column: "RoleId");

            migrationBuilder.CreateIndex(
                name: "RoleNameIndex",
                table: "AspNetRoles",
                column: "NormalizedName",
                unique: true);

            migrationBuilder.CreateIndex(
                name: "IX_AspNetUserClaims_UserId",
                table: "AspNetUserClaims",
                column: "UserId");

            migrationBuilder.CreateIndex(
                name: "IX_AspNetUserLogins_UserId",
                table: "AspNetUserLogins",
                column: "UserId");

            migrationBuilder.CreateIndex(
                name: "IX_AspNetUserRoles_RoleId",
                table: "AspNetUserRoles",
                column: "RoleId");

            migrationBuilder.CreateIndex(
                name: "EmailIndex",
                table: "AspNetUsers",
                column: "NormalizedEmail");

            migrationBuilder.CreateIndex(
                name: "UserNameIndex",
                table: "AspNetUsers",
                column: "NormalizedUserName",
                unique: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "AspNetRoleClaims");

            migrationBuilder.DropTable(
                name: "AspNetUserClaims");

            migrationBuilder.DropTable(
                name: "AspNetUserLogins");

            migrationBuilder.DropTable(
                name: "AspNetUserRoles");

            migrationBuilder.DropTable(
                name: "AspNetUserTokens");

            migrationBuilder.DropTable(
                name: "AspNetRoles");

            migrationBuilder.DropTable(
                name: "AspNetUsers");

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
    }
}
