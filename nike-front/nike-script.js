const words = ["จัดส่งฟรีแบบมาตรฐาน & คืนสินค้าฟรี 30 วัน", "เคลื่อนไหว เลือกซื้อ ออกแบบเอง และเฉลิมฉลองไปกับเรา", "สมาชิกใหม่รับส่วนลด 15% บน Nike App: ใช้โค้ด APP15"]
let index = 0

function changeword() {
    document.getElementById("textchange").textContent = words[index]
    index = (index + 1) % words.length
}

changeword()
setInterval(changeword, 5000)