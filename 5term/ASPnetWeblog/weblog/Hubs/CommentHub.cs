using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.SignalR;
using weblog.Models;

namespace weblog.Hubs
{
    public class CommentHub: Hub
    {
        private readonly AppDbContext _appDbContext;

        public CommentHub(AppDbContext appDbContext)
        {
            _appDbContext = appDbContext;
        }
        
        [Authorize]
        public async Task SendComment(Comment comment)
        {
            _appDbContext.Comments.Add(comment); 
            _appDbContext.SaveChanges();                                                          
            var username = Context.User?.Identity.Name; 
            await Clients.All.SendAsync("ReceiveMessage", comment, username);                     
        }
   
   
   }
}