#pragma checksum "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "70e31780fab2f35c3c60f69370c69f2352b5918f"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Shared__OneCardPartial), @"mvc.1.0.view", @"/Views/Shared/_OneCardPartial.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/_ViewImports.cshtml"
using weblog;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/_ViewImports.cshtml"
using weblog.Models;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/_ViewImports.cshtml"
using weblog.ViewModels;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/_ViewImports.cshtml"
using weblog.Pages;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/_ViewImports.cshtml"
using Microsoft.AspNetCore.Html;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"70e31780fab2f35c3c60f69370c69f2352b5918f", @"/Views/Shared/_OneCardPartial.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"ceed24db15becfdae846fe8d4c50132605152ee2", @"/Views/_ViewImports.cshtml")]
    public class Views_Shared__OneCardPartial : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<Post>
    {
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_0 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("asp-controller", "Post", global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_1 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("asp-action", "Detail", global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        #line hidden
        #pragma warning disable 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext __tagHelperExecutionContext;
        #pragma warning restore 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner __tagHelperRunner = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner();
        #pragma warning disable 0169
        private string __tagHelperStringValueBuffer;
        #pragma warning restore 0169
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __backed__tagHelperScopeManager = null;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __tagHelperScopeManager
        {
            get
            {
                if (__backed__tagHelperScopeManager == null)
                {
                    __backed__tagHelperScopeManager = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager(StartTagHelperWritingScope, EndTagHelperWritingScope);
                }
                return __backed__tagHelperScopeManager;
            }
        }
        private global::Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("\n<div class=\"col-4 card border-white one-card\">\n  <img");
            BeginWriteAttribute("src", "\n    src= \"", 66, "\"", 92, 1);
#nullable restore
#line 5 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
WriteAttributeValue("", 77, Model.ImageUrl, 77, 15, false);

#line default
#line hidden
#nullable disable
            EndWriteAttribute();
            BeginWriteAttribute("alt", "\n    alt=\"", 93, "\"", 103, 0);
            EndWriteAttribute();
            WriteLiteral("\n    class=\"card-img-top pt-3\"\n  />\n  <div class=\"card-body px-0\">\n    ");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("a", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "70e31780fab2f35c3c60f69370c69f2352b5918f4754", async() => {
                WriteLiteral("\n      <div class=\"card-title h4 text-dark\">");
#nullable restore
#line 11 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
                                      Write(Model.Title);

#line default
#line hidden
#nullable disable
                WriteLiteral("</div>\n      <div class=\"card-subtitle text-secondary h6\">\n        ");
#nullable restore
#line 13 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
   Write(Model.ShortDescription);

#line default
#line hidden
#nullable disable
                WriteLiteral("\n      </div>\n    ");
            }
            );
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper);
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.Controller = (string)__tagHelperAttribute_0.Value;
            __tagHelperExecutionContext.AddTagHelperAttribute(__tagHelperAttribute_0);
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.Action = (string)__tagHelperAttribute_1.Value;
            __tagHelperExecutionContext.AddTagHelperAttribute(__tagHelperAttribute_1);
            if (__Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.RouteValues == null)
            {
                throw new InvalidOperationException(InvalidTagHelperIndexerAssignment("asp-route-id", "Microsoft.AspNetCore.Mvc.TagHelpers.AnchorTagHelper", "RouteValues"));
            }
            BeginWriteTagHelperAttribute();
#nullable restore
#line 10 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
                                                   WriteLiteral(Model.PostId);

#line default
#line hidden
#nullable disable
            __tagHelperStringValueBuffer = EndWriteTagHelperAttribute();
            __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.RouteValues["id"] = __tagHelperStringValueBuffer;
            __tagHelperExecutionContext.AddTagHelperAttribute("asp-route-id", __Microsoft_AspNetCore_Mvc_TagHelpers_AnchorTagHelper.RouteValues["id"], global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\n    <div class=\"author mt-3 text-dark card-subtitle\">Author\'s Name</div>\n    <div class=\"mt-1 text-muted card-subtitle star\">\n      ");
#nullable restore
#line 18 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
 Write(Model.DatePosted.ToString("MMM dd"));

#line default
#line hidden
#nullable disable
            WriteLiteral(" · ");
#nullable restore
#line 18 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
                                        Write(Model.TimeToRead);

#line default
#line hidden
#nullable disable
            WriteLiteral(" min read ");
#nullable restore
#line 18 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
                                                                         if (Model.IsForSubscribersOnly){

#line default
#line hidden
#nullable disable
            WriteLiteral("                                                                          <span>★</span>\n");
#nullable restore
#line 20 "/home/qwerty/5semester/ASP.net C#/weblog/weblog/Views/Shared/_OneCardPartial.cshtml"
                                                                        }

#line default
#line hidden
#nullable disable
            WriteLiteral("    </div>\n  </div>\n</div>\n\n");
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<Post> Html { get; private set; }
    }
}
#pragma warning restore 1591