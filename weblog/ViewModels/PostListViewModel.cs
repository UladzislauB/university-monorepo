using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using weblog.Models;

namespace weblog.ViewModels
{
    public class PostListViewModel
    {
       public IEnumerable<Post> Posts { get; set; }
       
       public string CurrentCategory { get; set; }
    }
}