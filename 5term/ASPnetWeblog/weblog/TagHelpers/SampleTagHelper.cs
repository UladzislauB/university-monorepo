using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Razor.TagHelpers;

namespace weblog.TagHelpers
{
    public class SampleTagHelper : TagHelper
    {
        public List<String> AlternateClasses { get; set; }
        public List<string> Elements { get; set; }
        
        public override void Process(TagHelperContext context, TagHelperOutput output)
        {
            output.TagName = "table";
            output.TagMode = TagMode.StartTagAndEndTag;

            var index = 0;
            foreach (var elem in Elements)
            {
                output.Content.AppendHtml($"<tr class={AlternateClasses[index % 2]}><td>{elem}</td></tr>");
                index++;
            }

        }
    }
}