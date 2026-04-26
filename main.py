from pyscript import document

photos = document.getElementById("photos")


photos.innerHTML = """
<div class="row justify-content-center">
    <div class="col-md-5 mb-4" id="activity">
            <img src="Halloween.jpg"><br>
            <p><b>Halloween</b></p>
            <p class="sub">Oct. 24, 2025 | Kpop Demon Hunters!</p>
    </div>

    <div class="col-md-5 mb-4" id="activity">
            <img src="ChristmasParty.jpg"><br>
            <p><b>Christmas Party</b></p>
            <p class="sub">Dec. 18, 2025 | Sir De Guzman & Sir Gervacio</p>
    </div>

    <div class="col-md-5 mb-4" id="activity">
            <img src="MiniMart.jpg"><br>
            <p><b>Mini Mart and Food Fair</b></p>
            <p class="sub">Dec. 5, 2025 | Slam Dunk!</p>
    </div>

    <div class="col-md-5 mb-4" id="activity">
            <img src="GreenHornets.JPG"><br>
            <p><b>Intramurals</b></p>
            <p class="sub">March 26, 2026 | 10S & 11H</p>
    </div>
</div>
"""
