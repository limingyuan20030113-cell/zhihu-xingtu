from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/gemini', methods=['POST'])
def gemini_proxy():
    """
    无 API 模式下的智能模拟中枢
    """
    try:
        data = request.json
        prompt = data.get("prompt", "")

        # 1. 识别是否为“AI 智能测评页”发来的 IEP 定制请求
        if "IEP" in prompt or "干预目标" in prompt:
            if "delay" in prompt or "迟缓" in prompt:
                mock_text = """
                <div class="space-y-6 text-base sm:text-lg leading-loose">
                    <p class="text-gray-800 font-bold text-lg"><b>🎯 针对特征：</b>智力发育迟缓 / 肢体运动滞后阶段个案。</p>
                    <div class="p-6 bg-amber-50/60 rounded-2xl border-2 border-amber-200 shadow-sm">
                        <h5 class="font-black text-amber-950 text-lg mb-2">🌤️ 上午：09:30 · 串珠与手眼精细度抓握练习</h5>
                        <p class="text-gray-700"><b>【教学目标】</b>提升拇指与食指的对指力量，强化上肢手眼协调感知。</p>
                        <p class="text-gray-700"><b>【操作指南】</b>提供大孔径彩珠与粗绳，家长先进行完整示范。采用“小步骤拆分法”（Task Analysis），引导孩子独立穿过最后一步，完成时立即给予核心强化物（口头赞美/击掌）。</p>
                        <p class="text-amber-900 font-extrabold bg-amber-100/50 p-3 rounded-xl mt-2"><b>【正向强化话术】</b>“宝宝太棒了！你看，小红珠子自己穿过来了，和妈妈大力的击个掌！”</p>
                    </div>
                    <div class="p-6 bg-blue-50/60 rounded-2xl border-2 border-blue-200 shadow-sm">
                        <h5 class="font-black text-blue-950 text-lg mb-2">🥣 午餐：12:00 · 生活自理能力建构（勺子进食）</h5>
                        <p class="text-gray-700"><b>【教学目标】</b>建立独立自主进食行为链，消除抗拒情绪。</p>
                        <p class="text-gray-700"><b>【操作指南】</b>使用带防滑大柄的特制勺。家长由“手把手辅助”逐渐消退为“握住孩子手腕”，再消退至“触碰肘部”，引导其独立送入口中（逐步消退法）。</p>
                    </div>
                </div>
                """
            elif "adhd" in prompt or "多动" in prompt:
                mock_text = """
                <div class="space-y-6 text-base sm:text-lg leading-loose">
                    <p class="text-gray-800 font-bold text-lg"><b>🎯 针对特征：</b>注意力缺陷与多动倾向 / 情绪起伏冲动个案。</p>
                    <div class="p-6 bg-amber-50/60 rounded-2xl border-2 border-amber-200 shadow-sm">
                        <h5 class="font-black text-amber-950 text-lg mb-2">🌤️ 上午：10:30 · 纯净沙漏桌面专注任务</h5>
                        <p class="text-gray-700"><b>【教学目标】</b>延长视觉专注时间，建立“任务 - 强化”的契约意识。</p>
                        <p class="text-gray-700"><b>【操作指南】</b>完全清空书桌杂物，仅放置彩色积木。设置3-5分钟正向流速沙漏，承诺在沙漏漏完前保持在座位上，即可获得一枚“大星星代币”。</p>
                        <p class="text-amber-900 font-extrabold bg-amber-100/50 p-3 rounded-xl mt-2"><b>【正向强化话术】</b>“宝宝刚刚小屁股坐得真端正！你看沙漏结束了，你赢得了第一颗代币星星！”</p>
                    </div>
                </div>
                """
            else:
                mock_text = """
                <div class="space-y-6 text-base sm:text-lg leading-loose">
                    <p class="text-gray-800 font-bold text-lg"><b>🎯 针对特征：</b>孤独症谱系障碍（自闭倾向）/ 社交退缩个体。</p>
                    <div class="p-6 bg-amber-50/60 rounded-2xl border-2 border-amber-200 shadow-sm">
                        <h5 class="font-black text-amber-950 text-lg mb-2">🌤️ 上午：09:30 · 核心对视引导与共同注意力（JA）建立</h5>
                        <p class="text-gray-700"><b>【教学目标】</b>诱发自主、有社会性意图的眼神交流，改善机械性刻板避视。</p>
                        <p class="text-gray-700"><b>【操作指南】</b>将孩子最心爱的小汽车玩具举在家长双眼中央。当孩子出现追视，且眼神与家长对视长于1.5秒时，立刻将玩具交给他作为正向行为强化。</p>
                        <p class="text-amber-900 font-extrabold bg-amber-100/50 p-3 rounded-xl mt-2"><b>【正向强化话术】</b>“亮晶晶！宝宝刚刚看着妈妈的眼睛了！真棒，这辆小汽车现在奖励给你玩！”</p>
                    </div>
                </div>
                """
            return jsonify({"text": mock_text})

        # 2. 识别是否为右下角“星小护”发送的自由聊天咨询请求
        else:
            user_msg = prompt.lower()
            if "免费" in user_msg or "钱" in user_msg or "收费" in user_msg:
                reply = "家长您请一百个放心！❤️ 智护星途已经严格定位为纯公益民办非营利组织。我们连接高校的特教师资资源，为您提供的一对一个训匹配、居家IEP测评等服务是【全流程 100% 完全免费】的，中后期绝不收取任何费用。"
            elif "怎么申请" in user_msg or "报名" in user_msg or "加入" in user_msg or "志愿者" in user_msg:
                reply = "热烈欢迎加入我们！🌟 如果您是需要支持的特殊儿童家长，或者想要获取珍贵学分的高校研究生，可以直接点击我们网页顶部的【家长免费申请】或对应的专属按钮，直接填报腾讯官方登记问卷，我们会在24小时内联系您！"
            else:
                reply = "收到您的信赖倾诉啦，给您一个温暖的抱抱 🫂。陪伴特殊宝贝长大的道路虽然辛苦，但有我们多学科的研究生团队和胡学平、蔺红春等硕导专家库在背后为您提供长期的IEP教案把关与上门跟课，我们一起努力，让星星的孩子亮晶晶！✨"

            return jsonify({"text": reply})

    except Exception as e:
        return jsonify({"error": f"演示中枢偶发性波动: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)