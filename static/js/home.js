
let home_app = new Vue({
    el: "#home-app",
    data: {
        product:{
            products: [],
            title: "",
            category: undefined,
            subCategory: undefined
        },
        processing: false
    },
    methods: {
        getProducts: function (){
            let that = this;
            axios.get('/api/v1/product/', {
            })
            .then(function (response) {
                that.product.products = response.data;
            })
            .catch(function (response) {
                alert("something goes wrong");
            })
        },
        loadDataTable: function () {
            $(".customers").DataTable({
                 columnDefs: [ {
                    orderable: false,
                    className: 'select-checkbox',
                    targets:   0
                } ],
                select: {
                    style:    'os',
                    selector: 'td:first-child'
                },
                order: [[ 1, 'asc' ]],
                searching: false,
                paging: false,
                info: false
            });
        },
        saveProduct: function () {
            let that = this;
            that.processing = true;
            let body = {
               "product-title": $("#product-title").val(),
               "category": $("#category-select option:selected").val(),
               "sub-category": $("#sub-category-select option:selected").val(),

            };
            axios.post('/api/v1/product/', body)
            .then(function (response) {

                that.processing = false;
                window.location.reload()
            })
            .catch(function (response) {
                alert("Enter valid input");
            })
        },
        getCategories: function () {
            let that = this;
            axios.get('/api/v1/category/', {
            })
            .then(function (response) {
                $.each(response.data, function(key, value) {
                     $('#category-select')
                         .append($("<option></option>")
                                    .attr("value",value.id)
                                    .text(value.name));
                });
            })
            .catch(function (response) {
                alert("something goes wrong");
            })
        },
        getSubCategories: function () {
            let that = this;
            axios.get('/api/v1/sub-category/', {
            })
            .then(function (response) {
                $.each(response.data, function(key, value) {
                     $('#sub-category-select')
                         .append($("<option></option>")
                                    .attr("value",value.id)
                                    .text(value.name));
                });
            })
            .catch(function (response) {
                alert("something goes wrong");
            })
        }
    },
    mounted() {
        this.getProducts();
    }
});