const data = [
    {
        name: 'Adam',
        age: 20,
        salary: 30100
    },
    {
        name: 'Bob',
        age: 60,
        salary: 102000
    },
    {
        name: 'Carla',
        age: 31,
        salary: 57000
    },
    {
        name: 'Dave',
        age: 42,
        salary: 22000
    },
    {
        name: 'Ethel',
        age: 80,
        salary: 91000
    },
    {
        name: 'Frank',
        age: 28,
        salary: 73000
    },
    {
        name: 'Gina',
        age: 21,
        salary: 16000
    }
]

function favDisplay() {  
    var mylist = document.getElementById("myList");  
    // document.getElementById("favourite").value = mylist.options[mylist.selectedIndex].text; 
    if (mylist.options[mylist.selectedIndex].text == "Age") {
        data.sort(function(a, b) {
            return b.age - a.age;
          });
        document.getElementById('charts').innerHTML = data.map(user => 
            `<div class="container">
              <div class="name"> ${user.name} </div>
              <div class="bars" style=width:${(user.age / 10)*5}% > </div>
              <div class="data"> ${user.age} </div>
            </div>`
        ).join('') 
    } else if ((mylist.options[mylist.selectedIndex].text == "Salary")) {
        data.sort(function(a, b) {
            return b.salary - a.salary;
          });
        document.getElementById('charts').innerHTML = data.map(user => 
            `<div class="container">
              <div class="name"> ${user.name} </div>
              <div class="bars" style=width:${(user.salary / 10000) * 7}% > </div>
              <div class="data"> ${user.salary} </div>
            </div>`
        ).join('') 

    }

} 

