const accordionItemHeaders = document.querySelectorAll(
  ".accordion-item-header"
);

accordionItemHeaders.forEach((accordionItemHeader) => {
  accordionItemHeader.addEventListener("click", (event) => {
    // Uncomment in case you only want to allow for the display of only one collapsed item at a time!

    const currentlyActiveAccordionItemHeader = document.querySelector(
      ".accordion-item-header.active"
    );
    if (
      currentlyActiveAccordionItemHeader &&
      currentlyActiveAccordionItemHeader !== accordionItemHeader
    ) {
      currentlyActiveAccordionItemHeader.classList.toggle("active");
      currentlyActiveAccordionItemHeader.nextElementSibling.style.maxHeight = 0;
    }
    accordionItemHeader.classList.toggle("active");
    const accordionItemBody = accordionItemHeader.nextElementSibling;
    if (accordionItemHeader.classList.contains("active")) {
      accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
    } else {
      accordionItemBody.style.maxHeight = 0;
    }
  });
});
// Item Header

// Start Scrolling To Top
const scrolling = document.querySelector(".arrow");
const apperArrow = document.querySelector(".appear");
function scrollToTop(ar) {
  window.addEventListener("scroll", () => {
    if (window.scrollY >= document.body.offsetTop + 300) {
      ar.classList.add("appear");
    } else {
      ar.classList.remove("appear");
    }
  });

  ar.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
}
scrollToTop(scrolling);
// End Scrolling To Top

// Start Fetch On Data Products
const siteLink = document.getElementById("siteLink").href;
fetch(`${siteLink}api/method/directory_client.api.products`)
  .then((response) => response.json())
  .then((data) => {
    if (data.message == "") {
      // row
      const rows = document.getElementById("row");
      // col
      const col = document.createElement("div");
      col.className = `col-12 mb-4 ps-0`;
      rows.appendChild(col);
      // box
      const mainProduct = document.createElement("div");
      mainProduct.appendChild(document.createTextNode("No Products Available"));
      mainProduct.className = `box m-auto overflow-hidden d-flex align-items-center justify-content-center`;
      mainProduct.style.height = `500px`;
      mainProduct.style.fontSize = `2rem`;
      mainProduct.style.fontWeight = `bold`;
      mainProduct.style.margin = `auto`;
      col.appendChild(mainProduct);
    } else {
      data.message.forEach((repo) => {
        // row
        const row = document.getElementById("row");
        // col
        const col = document.createElement("div");
        col.className = `col-md-6 col-lg-4 mb-4 ps-0`;
        row.appendChild(col);
        // box
        const mainProduct = document.createElement("div");
        mainProduct.className = `box m-auto d-flex card border overflow-hidden`;
        mainProduct.style.height = `625px`;
        mainProduct.style.gap = `1rem`;
        col.appendChild(mainProduct);
        // pic
        const link = document.createElement("a");
        link.href = `${repo.site_name}/${repo.route}`;
        link.setAttribute("target", "blank");
        const mainPic = document.createElement("div");
        const mainImg = document.createElement("img");
        mainImg.className = `mw-100 w-100`;
        mainImg.style.height = "200px";
        mainImg.style.objectFit = "contain";
        mainImg.src = `${repo.site_name}${repo.website_image}`;
        mainPic.appendChild(mainImg);
        link.appendChild(mainPic);
        mainProduct.appendChild(link);
        // head
        const linkHeadOne = document.createElement("a");
        linkHeadOne.href = `${repo.site_name}/${repo.route}`;
        linkHeadOne.setAttribute("target", "blank");
        linkHeadOne.className = `desc d-flex flex-column gap-2 border-top`;
        linkHeadOne.style.height = `85px`;
        linkHeadOne.style.overflow = `hidden`;
        const head = document.createElement("h5");
        head.className = `ps-3 pt-2 text-black`;
        head.appendChild(document.createTextNode(repo.item_name));
        linkHeadOne.appendChild(head);
        mainProduct.appendChild(linkHeadOne);
        // Desc
        const linkHeadTwo = document.createElement("a");
        linkHeadTwo.href = `${repo.site_name}/${repo.route}`;
        linkHeadTwo.setAttribute("target", "blank");
        linkHeadTwo.className = `desc d-flex flex-column gap-2`;
        const mainP = document.createElement("p");
        mainP.style.height = `188px`;
        mainP.className = `mb-4 pe-3 ps-3 text-secondary`;
        mainP.style.overflow = `hidden`;
        mainP.style.textOverflow = `ellipsis`;
        function removeTags(str) {
          if (str === null || str === "") return false;
          else str = str.toString();

          // Regular expression to identify HTML tags in
          // the input string. Replacing the identified
          // HTML tag with a null string.
          return str.replace(/(<([^>]+)>)/gi, "");
        }
        mainP.appendChild(
          document.createTextNode(removeTags(repo.description))
        );
        linkHeadTwo.appendChild(mainP);
        mainProduct.appendChild(linkHeadTwo);

        // Learn more
        const linkThree = document.createElement("a");
        linkThree.href = `/company/product-details/${repo.name}`;
        linkThree.setAttribute("target", "blank");
        linkThree.className = `btn main-btn d-flex align-items-center justify-content-center ms-3`;
        linkThree.style.width = `fit-content`;
        linkThree.style.marginBottom = `1rem`;
        linkThree.appendChild(document.createTextNode(`Learn More`));
        mainProduct.appendChild(linkThree);
        // Any Div
        const nameDiv = document.createElement("div");
        nameDiv.id = `name-product`;
        nameDiv.appendChild(document.createTextNode(repo.name));
        nameDiv.style.display = `none`;
        mainProduct.appendChild(nameDiv);
      });
    }
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
    // row
    const rows = document.getElementById("row");
    // col
    const col = document.createElement("div");
    col.className = `col-12 mb-4 ps-0`;
    rows.appendChild(col);
    // box
    const mainProduct = document.createElement("div");
    mainProduct.appendChild(document.createTextNode("No Products Available"));
    mainProduct.className = `box m-auto overflow-hidden d-flex align-items-center justify-content-center`;
    mainProduct.style.height = `500px`;
    mainProduct.style.fontSize = `2rem`;
    mainProduct.style.fontWeight = `bold`;
    mainProduct.style.margin = `auto`;
    col.appendChild(mainProduct);
  });
// End Fetch On Data Products

// Start Fetch On Data Blogs
fetch(`${siteLink}api/method/directory_client.api.blog`)
  .then((response) => response.json())
  .then((repos) => {
    if (repos.message == "") {
      // row
      const rows = document.getElementById("rows");
      // col
      const col = document.createElement("div");
      col.className = `col-12 mb-4 ps-0`;
      rows.appendChild(col);
      // box
      const mainProduct = document.createElement("div");
      mainProduct.appendChild(document.createTextNode("No Blogs Available"));
      mainProduct.className = `box m-auto overflow-hidden d-flex align-items-center justify-content-center`;
      mainProduct.style.height = `500px`;
      mainProduct.style.fontSize = `2rem`;
      mainProduct.style.fontWeight = `bold`;
      mainProduct.style.margin = `auto`;
      col.appendChild(mainProduct);
    } else {
      repos.message.forEach((repos) => {
        // row
        const rows = document.getElementById("rows");
        // col
        const col = document.createElement("div");
        col.className = `col-md-6 col-lg-4 mb-4 ps-0`;
        rows.appendChild(col);
        // box
        const mainProduct = document.createElement("div");
        mainProduct.className = `box m-auto card border overflow-hidden`;
        mainProduct.style.height = `500px`;
        col.appendChild(mainProduct);
        // pic
        const link = document.createElement("a");
        link.href = `${repos.site_name}/${repos.route}`;
        link.setAttribute("target", "blank");
        const mainPic = document.createElement("div");
        const mainImg = document.createElement("img");
        mainImg.className = `mw-100 w-100`;
        mainImg.style.height = "200px";
        mainImg.style.objectFit = "cover";
        mainImg.src = `${repos.site_name}/${repos.meta_image}`;
        mainPic.appendChild(mainImg);
        link.appendChild(mainPic);
        mainProduct.appendChild(link);
        // head
        const linkHeadOne = document.createElement("a");
        linkHeadOne.href = `${repos.site_name}/${repos.route}`;
        linkHeadOne.setAttribute("target", "blank");
        linkHeadOne.className = `desc d-flex flex-column gap-2 border-top`;
        linkHeadOne.style.overflow = `hidden`;
        const head = document.createElement("h5");
        head.className = `ps-3 pt-2 pe-3 text-black`;
        head.appendChild(document.createTextNode(repos.title));
        linkHeadOne.appendChild(head);
        mainProduct.appendChild(linkHeadOne);
        // Desc
        const linkHeadTwo = document.createElement("a");
        linkHeadTwo.href = `${repos.site_name}/${repos.route}`;
        linkHeadTwo.setAttribute("target", "blank");
        linkHeadTwo.className = `desc d-flex flex-column gap-2`;
        const mainP = document.createElement("p");
        mainP.style.height = `188px`;
        mainP.className = `mb-4 p-3 text-secondary`;
        mainP.style.overflow = `hidden`;
        mainP.style.textOverflow = `ellipsis`;
        function removeTags(str) {
          if (str === null || str === "") return false;
          else str = str.toString();

          // Regular expression to identify HTML tags in
          // the input string. Replacing the identified
          // HTML tag with a null string.
          return str.replace(/(<([^>]+)>)/gi, "");
        }
        mainP.appendChild(document.createTextNode(removeTags(repos.content)));
        linkHeadTwo.appendChild(mainP);
        mainProduct.appendChild(linkHeadTwo);
      });
    }
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
    // row
    const rows = document.getElementById("rows");
    // col
    const col = document.createElement("div");
    col.className = `col-12 mb-4 ps-0`;
    rows.appendChild(col);
    // box
    const mainProduct = document.createElement("div");
    mainProduct.appendChild(document.createTextNode("No Blogs Available"));
    mainProduct.className = `box m-auto overflow-hidden d-flex align-items-center justify-content-center`;
    mainProduct.style.height = `500px`;
    mainProduct.style.fontSize = `2rem`;
    mainProduct.style.fontWeight = `bold`;
    mainProduct.style.margin = `auto`;
    col.appendChild(mainProduct);
  });

// End Fetch On Data Blogs

//contact form
const contactButton = document.getElementById("contactButton");
console.log(siteLink);
contactButton.addEventListener("click", (el) => {
  el.preventDefault();
  fetch(`${siteLink}api/method/directory_client.api.contact`, {
    method: "POST",
    body: JSON.stringify({
      first_name: document.querySelector("input[id='firstName']").value,
      last_name: document.querySelector("input[id='lastName']").value,
      phone: document.querySelector("input[id='phone']").value,
      company: document.querySelector("input[id='companyName']").value,
      job_title: document.querySelector("input[id='jobTitle']").value,
      email: document.querySelector("input[id='Email']").value,
      subject: document.getElementById("Subject").value,
      description: document.getElementById("textArea").value,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) =>
      Swal.fire(
        "Thanks for Contact Us.",
        "We Will be in Touch Shortly.",
        "success"
      )
    );
});
