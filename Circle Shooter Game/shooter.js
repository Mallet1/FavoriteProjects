class Fire {
    constructor(radius, x, y, color, xChange, yChange, gravity){
        this.radius = radius
        this.x = x;
        this.y = y;
        this.color = color;
        this.xChange = xChange
        this.yChange = yChange
        this.gravity = gravity;
        this.opacity = 1;
    }

    move(){
        this.x += this.xChange;
        this.y += this.yChange;
        this.yChange += this.gravity
    }

    draw(){
        ctx.beginPath();
        ctx.lineWidth = this.radius * 2
        ctx.strokeStyle = this.color.substring(0, this.color.length-2) + this.opacity + ')'
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
        ctx.stroke();
    }

    isOffScreen() {
        return (this.x < 0 ||
            this.x > canvas.width ||
            this.y < 0 ||
            this.y > canvas.height)
    }

    getRect() {
        return {
            top : this.y - this.radius * 2,
            left : this.x - this.radius * 2,
            width : this.radius * 4,
            height : this.radius * 4
        }
    }
}

window.onload = function() {
    document.addEventListener("keydown", keyPush);
    document.addEventListener("keyup", keyLift);
}


let canvas = document.getElementById("canvas")
let ctx = canvas.getContext("2d");

let scoreEl = document.getElementById("scoreEl")
console.log(scoreEl)
let score = 0
var start = new Date();
let mouseX = 0
let mouseY = 0

let allFires = []
let enemies = []
let particles = []
let defaultRadius = 10 // the radius when put into the arc function above is off
let maximumenemyCount = 10
let fireSpeed = 10

let playerAcc = 0.2
let playerFriction = playerAcc / 4
let centerBall = new Fire(defaultRadius,
                        canvas.width/2, canvas.height/2,
                        "rgba(255,255,255,1)",
                        0, 0, 0)

let fps = 60

let mouseDown = false
canvas.addEventListener("mousedown", function() {
    createFire()
    mouseDown = true
})

canvas.addEventListener("mouseup", function() {
    mouseDown = false
})

canvas.addEventListener("mousemove", function(e) {
    mouseX = e.clientX
    mouseY = e.clientY
})

w = a = s = d = false

function keyPush(evt) {
    switch(evt.keyCode) {
        case 87:
            w = true
            break;
        case 65:
            a = true
            break;
        case 83:
            s = true
            break;
        case 68:
            d = true
            break;
    }
}

function keyLift(evt) {
    switch(evt.keyCode) {
        case 87:
            w = false
            break;
        case 65:
            a = false
            break;
        case 83:
            s = false
            break;
        case 68:
            d = false
            break;
    }
}

let gameLoop = function() {
    setInterval(show, 1000/fps)
}

let show = function() {
    update();
    draw();
}

function createFire() {
    const angle = Math.atan2(mouseY - centerBall.y,
                            mouseX - centerBall.x) // angle from center ball to mouse position

    // use sin and cos to calculate the horizontal and verticle velocities
    const xChange = Math.cos(angle) * fireSpeed
    const yChange = Math.sin(angle) * fireSpeed

    let fire = new Fire(defaultRadius/5,
        centerBall.x, centerBall.y,
        centerBall.color,
        xChange, yChange, 0
        )

    allFires.push(fire)
}

let automaticFire = function() {
    if (mouseDown) {
        let end = new Date();
        let time = end - start
        if (time % 5 == 0) {
            createFire()
        }
    }
}

let getRandColor = function() {
    let colors = ["rgba(255,0,0,1)",
                "rgba(0,255,0,1)",
                "rgba(0,0,255,1)",
                "rgba(255,255,0,1)",
                "rgba(0,255,255,1)",
                "rgba(255,165,0,1)",
                "rgba(255,105,180,1)"]

    return colors[parseInt(Math.random() * (colors.length - 1))]
}

let isCollision = function(a, b) {
    return !(
        ((a.top + a.height) < (b.top)) ||
        (a.top > (b.top + b.height)) ||
        ((a.left + a.width) < b.left) ||
        (a.left > (b.left + b.width))
    )
}

let animateExplosion = function(entity, color, radius) {
    let currentX = entity.x
    let currentY = entity.y

    let particle_amt = parseInt(Math.random() * 5 + 10)

    for (let i = 0; i < particle_amt; i++) {
        let xChange = (Math.random() - 0.5) * 10;
        let yChange = (Math.random() - 0.5) * 10;
        let entity = new Fire(radius,
                            currentX,
                            currentY, 
                            color,
                            xChange,
                            yChange,
                            0.1)

        particles.push(entity);
    }
}

let update = function() {
    ctx.fillStyle = 'rgba(0,0,0,0.3)'
    ctx.fillRect(0,0, canvas.width, canvas.height)

    if (enemies.length < maximumenemyCount) {
        let radius = parseInt(Math.random() * 10 + 5)
        
        let enemyX = Math.random() * canvas.width
        let enemyY = Math.random() * canvas.height

        while (Math.abs(centerBall.x - enemyX) < 200) enemyX = Math.random() * canvas.width
        while (Math.abs(centerBall.y - enemyY) < 200) enemyY = Math.random() * canvas.height

        const angle = Math.atan2(centerBall.y - enemyY,
                                centerBall.x - enemyX)

        const xChange = Math.cos(angle) * (Math.abs(radius-14.5) * 0.2)
        const yChange = Math.sin(angle) * (Math.abs(radius-14.5) * 0.2)

        let enemy = new Fire(radius,
                            enemyX, enemyY,
                            getRandColor(),
                            xChange, yChange, 0)

        enemies.push(enemy)
    }

    if (mouseDown) {
        setTimeout(() => {
            automaticFire()
        }, 1000);
    }
    // else

    for (let i = 0; i < allFires.length; i++) {
        if (allFires[i].isOffScreen()) allFires.splice(i, 1)
        else allFires[i].move()

        for (let k = 0; k < enemies.length; k++) {
            if (typeof(allFires[i]) != "undefined" && isCollision(enemies[k].getRect(), allFires[i].getRect())) {
                score += 100
                animateExplosion(allFires[i], enemies[k].color, 1)
                allFires.splice(i, 1)
                if (enemies[k].radius >= 5) enemies[k].radius -= 2
                if (enemies[k].radius < 5) {
                    if (enemies[k].radius > 2) score += 1000
                    enemies.splice(k, 1)
                }

                scoreEl.innerHTML = score // changes the text in the scoreEl element
            }
        }
    }

    for (let i = 0; i < enemies.length; i++) {
        let angle = Math.atan2(centerBall.y - enemies[i].y,
            centerBall.x - enemies[i].x)
    
        enemies[i].xChange = Math.cos(angle) * (Math.abs(enemies[i].radius-20) * 0.35)
        enemies[i].yChange = Math.sin(angle) * (Math.abs(enemies[i].radius-20) * 0.35)

        if (enemies[i].radius >= 12) {
            let shootChance = parseInt(Math.random() * 200)

            if (shootChance == 0) {
                let enemy = new Fire(2,
                    enemies[i].x, enemies[i].y,
                    enemies[i].color,
                    0, 0, 0)

                enemies.push(enemy)
            }
        }

        if (enemies[i].isOffScreen() || isCollision(enemies[i].getRect(), centerBall.getRect())) {
            centerBall.radius--
            animateExplosion(enemies[i], enemies[i].color, parseInt(enemies[i].radius / 3))
            enemies.splice(i, 1)
        }
        else enemies[i].move()
    }

    for (let i = 0; i < particles.length; i++) {
        particles[i].move()
        particles[i].opacity -= 0.05
        if (particles[i].opacity <= 0) particles.splice(i, 1)
    }

    if (true) { // repetative stuff
        if (w) centerBall.yChange -= playerAcc
        if (a) centerBall.xChange -= playerAcc
        if (s) centerBall.yChange += playerAcc
        if (d) centerBall.xChange += playerAcc

        if (centerBall.xChange > 6) centerBall.xChange = 6
        if (centerBall.yChange > 6) centerBall.yChange = 6
        if (centerBall.xChange < -6) centerBall.xChange = -6
        if (centerBall.yChange < -6) centerBall.yChange = -6

        if (centerBall.xChange > 0) centerBall.xChange -= playerFriction
        if (centerBall.yChange > 0) centerBall.yChange -= playerFriction
        if (centerBall.xChange < 0) centerBall.xChange += playerFriction
        if (centerBall.yChange < 0) centerBall.yChange += playerFriction

        playerFriction = playerAcc / 4

        if (centerBall.x <= 0) {
            centerBall.x = 0.01; 
            centerBall.xChange = 0
        }

        if (centerBall.y <= 0) {
            centerBall.y = 0.01;
            centerBall.yChange = 0
        }

        if (centerBall.x >= canvas.width) {
            centerBall.x = canvas.width - 0.01;
            centerBall.xChange = 0
        }

        if (centerBall.y >= canvas.height) {
            centerBall.y = canvas.height - 0.01;
            centerBall.yChange = 0
        }
    }

    if (centerBall.radius < 5) {
        centerBall.radius = defaultRadius
        score = 0
    }
    centerBall.move()
}

let draw = function() {  
    allFires.forEach(fire=>{ 
        fire.draw();
    })

    enemies.forEach(enemy=>{
        enemy.draw();
    })

    particles.forEach(particle=>{
        particle.draw();
    })

    centerBall.draw()
}

gameLoop()
