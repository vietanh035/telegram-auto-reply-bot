import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv('BOT_TOKEN')

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Chào bạn! Gửi mã đơn + yêu cầu (tăng tốc, bảo hành, hủy, fake) để tôi trả lời.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower().strip()
    parts = text.split(maxsplit=1)
    if len(parts) != 2:
        update.message.reply_text("Vui lòng gửi đúng định dạng: Mã đơn + yêu cầu")
        return
    order_id, request = parts
    if request == 'tăng tốc':
        reply = f"Đơn hàng của bạn đã được đưa vào hàng chờ tăng tốc. Vui lòng chờ thêm một chút thời gian, chúng tôi sẽ cố gắng hoàn thành nhanh nhất có thể. Cảm ơn bạn đã kiên nhẫn."
    elif request == 'hủy':
        reply = f"Đơn hàng của bạn đã được đưa vào hàng chờ hủy. Thời gian hủy có thể kéo dài từ 0 đến 24 giờ, thậm chí lâu hơn. Bạn chỉ cần gửi yêu cầu hủy một lần, chúng tôi sẽ theo dõi và xử lý. Cảm ơn bạn đã thông cảm."
    elif request == 'bảo hành':
        reply = f"Đơn hàng của bạn đã được đưa vào hàng chờ bảo hành, sẽ mất một ít thời gian để hoàn tất. Nếu bảo hành không thành công, bạn sẽ được hoàn tiền một phần. Nếu dịch vụ không hỗ trợ bảo hành, đơn hàng sẽ không thể bảo hành. Chúng tôi sẽ cập nhật thông tin sớm nhất."
    elif request == 'fake':
        reply = f"Đơn hàng của bạn đã được gửi đến Admin để xử lý. Cảm ơn bạn đã kiên nhẫn chờ đợi. Chúng tôi sẽ cập nhật thông tin sớm nhất."
    else:
        reply = "Yêu cầu không hợp lệ. Vui lòng gửi yêu cầu đúng: tăng tốc, bảo hành, hủy, hoặc fake."
    update.message.reply_text(reply)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
