// setTimeout(function() {
//     $('#messages').fadeOut('slow');
//  }, 2000);

//  //Get search frm and page links
let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link'); 

if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault();
    //   console.log('Button Clicked');

      //GET DATA ATTRIBUTE
      let page = this.dataset.page
    //   console.log('page' , page)

    //ADD hidden search input to form
    searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

    //SUBMIT FROM
    searchForm.submit()
    });
  }
}


