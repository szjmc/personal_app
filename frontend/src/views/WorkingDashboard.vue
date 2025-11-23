<template>
  <div style="padding: 20px; min-height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
    <div style="max-width: 1200px; margin: 0 auto;">
      <div style="background: white; padding: 20px; border-radius: 16px; margin-bottom: 20px;">
        <h1 style="color: #333; margin-bottom: 10px;">个人管理应用仪表盘</h1>
        <p style="color: #666;">欢迎使用个人管理系统！</p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h2 style="color: #333; margin-bottom: 10px;">📋 任务管理</h2>
          <p style="color: #666;">管理您的日常任务和待办事项</p>
          <button @click="goToTasks" style="margin-top: 10px; padding: 8px 16px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            查看任务
          </button>
        </div>
        
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h2 style="color: #333; margin-bottom: 10px;">📅 日历管理</h2>
          <p style="color: #666;">查看和管理您的日程安排</p>
          <button @click="goToCalendar" style="margin-top: 10px; padding: 8px 16px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            查看日历
          </button>
        </div>
        
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h2 style="color: #333; margin-bottom: 10px;">📚 知识库</h2>
          <p style="color: #666;">记录和管理您的知识笔记</p>
          <button @click="goToKnowledge" style="margin-top: 10px; padding: 8px 16px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            查看知识库
          </button>
        </div>
        
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h2 style="color: #333; margin-bottom: 10px;">💰 财务管理</h2>
          <p style="color: #666;">跟踪您的收入和支出</p>
          <button @click="goToFinance" style="margin-top: 10px; padding: 8px 16px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            查看财务
          </button>
        </div>
        
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h2 style="color: #333; margin-bottom: 10px;">🏃‍♂️ 健康管理</h2>
          <p style="color: #666;">记录健康数据和运动习惯</p>
          <button @click="goToHealth" style="margin-top: 10px; padding: 8px 16px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            查看健康
          </button>
        </div>
        
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h2 style="color: #333; margin-bottom: 10px;">⚙️ 个人设置</h2>
          <p style="color: #666;">管理您的个人偏好和设置</p>
          <button @click="goToProfile" style="margin-top: 10px; padding: 8px 16px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            查看设置
          </button>
        </div>
      </div>
      
      <!-- 全景控制台入口 -->
      <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 16px; margin-top: 20px; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.15);">
        <button @click="goToCommandCenter" style="padding: 15px 30px; background: rgba(255,255,255,0.9); color: #667eea; border: none; border-radius: 12px; cursor: pointer; font-size: 16px; font-weight: bold; transition: all 0.3s; box-shadow: 0 4px 16px rgba(0,0,0,0.1);"
                @mouseover="$event.currentTarget.style.transform = 'scale(1.05)'" 
                @mouseleave="$event.currentTarget.style.transform = 'scale(1)'">
          🎛️ 进入全景控制台
        </button>
        <p style="color: rgba(255,255,255,0.8); margin-top: 15px; font-size: 14px;">
          一站式数据管理 · 快速操作 · 智能洞察
        </p>
      </div>
      
      <div style="text-align: center; margin-top: 30px;">
        <button @click="logout" style="padding: 12px 24px; background: #ef4444; color: white; border: none; border-radius: 8px; cursor: pointer;">
          退出登录
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      console.log('退出登录')
      this.$router.push('/login')
    },
    goToTasks() {
      console.log('跳转到任务管理')
      this.$router.push('/tasks')
    },
    goToCalendar() {
      console.log('跳转到日历管理')
      this.$router.push('/calendar')
    },
    goToKnowledge() {
      console.log('跳转到知识库')
      this.$router.push('/knowledge')
    },
    goToFinance() {
      console.log('跳转到财务管理')
      this.$router.push('/finance')
    },
    goToHealth() {
      console.log('跳转到健康管理')
      this.$router.push('/health')
    },
    goToProfile() {
      console.log('跳转到个人设置')
      this.$router.push('/profile')
    },
    goToCommandCenter() {
      console.log('跳转到全景控制台')
      this.$router.push('/command-center')
    }
  }
}
</script>