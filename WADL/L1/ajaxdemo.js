let obj = new XMLHttpRequest()

// obj.open("GET",)
obj.open("GET","a.txt")

obj.send()

obj.onload = function () {
    // alert("Heyyy ! this is ajax demo")
    console.log("inside ajax");
}