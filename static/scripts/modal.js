// Get the modal
var modal = document.getElementById('myModal');
var endModal = document.getElementById('endSubscriptionModal');
// Get the button that opens the modal
var btn = document.getElementById("myBtn");
var endBtn = document.getElementsByClassName("end-btn-smallest");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var i;
for(i=0;i<endBtn.length;i++)
{
    endBtn[i].onclick = function() {
        var item = $(this).closest("tr").text();
        var list = item.split('\n');
        var endSubPlanName = document.getElementById("endSubPlanName");
        var endSubPlanId = document.getElementById("endSubPlanId");
        endSubPlanName.value=list[1].trim();
        endSubPlanId.value=list[2].trim();
        endModal.style.display = "block";
    }
}

// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    else if(event.target == endModal) {
        endModal.style.display = "none";
    }
}
