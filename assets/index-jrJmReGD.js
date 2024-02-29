(function polyfill() {
  const relList = document.createElement("link").relList;
  if (relList && relList.supports && relList.supports("modulepreload")) {
    return;
  }
  for (const link of document.querySelectorAll('link[rel="modulepreload"]')) {
    processPreload(link);
  }
  new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type !== "childList") {
        continue;
      }
      for (const node of mutation.addedNodes) {
        if (node.tagName === "LINK" && node.rel === "modulepreload")
          processPreload(node);
      }
    }
  }).observe(document, { childList: true, subtree: true });
  function getFetchOpts(link) {
    const fetchOpts = {};
    if (link.integrity)
      fetchOpts.integrity = link.integrity;
    if (link.referrerPolicy)
      fetchOpts.referrerPolicy = link.referrerPolicy;
    if (link.crossOrigin === "use-credentials")
      fetchOpts.credentials = "include";
    else if (link.crossOrigin === "anonymous")
      fetchOpts.credentials = "omit";
    else
      fetchOpts.credentials = "same-origin";
    return fetchOpts;
  }
  function processPreload(link) {
    if (link.ep)
      return;
    link.ep = true;
    const fetchOpts = getFetchOpts(link);
    fetch(link.href, fetchOpts);
  }
})();
function renderTable(data) {
  const container = document.querySelector("#stockTable");
  const [start, end] = data;
  const gains = +end.Close ? Math.floor((+end.Close - +start.Close) / +start.Close * 100) : 0;
  container.innerHTML = `
  <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
  <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
    <tr>
      <th scope="col" class="px-6 py-3">
        Date
      </th>
      <th scope="col" class="px-6 py-3">
        Open
      </th>
      <th scope="col" class="px-6 py-3">
        High
      </th>
      <th scope="col" class="px-6 py-3">
        Close
      </th>
    </tr>
  </thead>
  <tbody>
    ${data.map((item) => `<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
      <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
        ${item.star_data || item.end_data}
      </th>
      <td class="px-6 py-4">
        ${item.Open}
      </td>
      <td class="px-6 py-4">
        ${item.High}
      </td>
      <td class="px-6 py-4">
        ${item.Close}
      </td>
    </tr>`).join("")}
    
    <tr class="bg-white text-center dark:bg-gray-800">
      <th scope="row" colspan="4" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
        ${gains}%
      </th>
    </tr>
  </tbody>
</table>
  `;
}
document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  fetch("/stock", {
    method: "POST",
    body: new FormData(e.target)
  }).then((response) => {
    if (response.ok) {
      return response.json();
    }
    throw new Error("Network response was not ok.");
  }).then((data) => {
    renderTable(data.list);
  }).catch((error) => {
    alert(`There has been a problem with your fetch operation: ${error}`);
  });
});
