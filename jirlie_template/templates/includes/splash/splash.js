// let carouselInner = document.querySelector(".carousel-inner");

// fetch("https://api.github.com/users/HossaamHassan/repos")
// .then((response) => response.json())
// .then((data) => {
//     data.forEach((repo, index) => {
//         let caourselItem = document.createElement("div");
//         if (index === 0) {
//             caourselItem.className = `carousel-item active`
//         } else {
//             caourselItem.className = `carousel-item `;
//         }
//         // let caourselItem = document.createElement("div");
//         caourselItem.appendChild(document.createTextNode(repo.name));
//         carouselInner.appendChild(caourselItem)
//     })
// })

// window.addEventListener("load", () => {
//     const loader = document.querySelector(".loader");
//     loader.classList.add("loader-hidden");
//     loader.addEventListener("transitionend", () => {
//         document.body.removeChild("loader");
//     })
// })
const video = document.getElementById("loading-video");
const content = document.getElementById("content");

video.addEventListener("ended", () => {
  document.getElementById("loader").style.display = `none`;
  content.style.display = `block`;
});
// window.addEventListener("load", () => {
//   document.getElementById("loader").style.display = `none`;
//   content.style.display = `block`;
// });
// let countries = document.querySelector(".countries");
// console.log(countries);
// fetch("./country_info.json")
//   .then((response) => response.json())
//   .then((data) => {
//     Object.entries(data).forEach((arr) => {
//       let spanCountry = document.createElement("span");
//       spanCountry.className = `country`;
//       spanCountry.appendChild(document.createTextNode(arr[0]));
//       countries.appendChild(spanCountry);
//       let spanIsd = document.createElement("span");
//       spanIsd.className = `isd`;
//       spanIsd.appendChild(document.createTextNode(arr[1].isd));
//       countries.appendChild(spanIsd);
//     });
//   });
