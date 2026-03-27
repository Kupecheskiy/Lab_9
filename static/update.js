// function updateProd(el) {
//     let product_id = el.value
//     fetch('/in_stock/' + product_id, {
//         method: 'patch',
//         headers: {'Content-type': 'application/json'},
//         body: JSON.stringify({'in_stock': el.checked})
//     })
//     // console.log(product_id)
// }

function addCompany() {
    let companyName = document.getElementById('company_name').value
    let term = document.getElementById('term').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify({'company_name': companyName, 'term': term})
    })
    console.log("Add")
}

function clearCompanies() {
    fetch('/clear', {
        method: 'DELETE'
    })
    .then(function(response) {
        if (response.ok) {
            location.reload();
        }
    });
}