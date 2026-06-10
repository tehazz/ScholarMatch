async function predictScholarship(){

    document.getElementById("loading").style.display = "block";
    document.getElementById("resultBox").style.display = "none";

    const data = {

        GPA: document.getElementById("gpa").value,
        Income: document.getElementById("income").value,
        COCU: document.getElementById("cocu").value,
        Kulliyyah: document.getElementById("kulliyyah").value,
        Year: document.getElementById("year").value
    };

    try{

        const response = await fetch("/predict",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("loading").style.display = "none";

        document.getElementById("resultBox").style.display = "block";

        if(result.error){

            document.getElementById("prediction").innerHTML =
                "Error: " + result.error;

            return;
        }

        document.getElementById("prediction").innerHTML =
            "Recommended Scholarship: " + result.prediction;

        document.getElementById("confidence").innerHTML =
            "Matching Score: " + result.confidence + "%";

    }

    catch(error){

        console.log(error);

        document.getElementById("loading").style.display = "none";

        alert("Something went wrong.");
    }
}