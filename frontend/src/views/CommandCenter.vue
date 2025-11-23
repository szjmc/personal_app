<template>
  <div style="padding: 20px; min-height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
    <div style="max-width: 1400px; margin: 0 auto;">
      <!-- 头部控制区 -->
      <div style="background: white; padding: 25px; border-radius: 16px; margin-bottom: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <div style="display: flex; align-items: center; gap: 20px;">
            <h1 style="color: #333; margin: 0; font-size: 28px;">🎛️ 个人数据全景控制台</h1>
            <div style="display: flex; gap: 10px;">
              <button @click="userMode = 'work'" :style="userMode === 'work' ? 'background: #3b82f6;' : 'background: #e5e7eb;'" style="padding: 8px 16px; border: none; border-radius: 20px; cursor: pointer; font-size: 12px; color: white;">
                💼 工作导向
              </button>
              <button @click="userMode = 'health'" :style="userMode === 'health' ? 'background: #10b981;' : 'background: #e5e7eb;'" style="padding: 8px 16px; border: none; border-radius: 20px; cursor: pointer; font-size: 12px; color: white;">
                🏃‍♂️ 健康导向
              </button>
              <button @click="userMode = 'all'" :style="userMode === 'all' ? 'background: #8b5cf6;' : 'background: #e5e7eb;'" style="padding: 8px 16px; border: none; border-radius: 20px; cursor: pointer; font-size: 12px; color: white;">
                🌟 全能型
              </button>
            </div>
          </div>
          <div style="display: flex; gap: 10px;">
            <button @click="refreshData" style="padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 8px; cursor: pointer;">
              🔄 刷新数据
            </button>
            <button @click="backToDashboard" style="padding: 10px 20px; background: #ef4444; color: white; border: none; border-radius: 8px; cursor: pointer;">
              返回仪表盘
            </button>
          </div>
        </div>

        <!-- 快速统计 -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px;">
          <div style="text-align: center; padding: 15px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #3b82f6;">
            <div style="font-size: 24px; font-weight: bold; color: #3b82f6; margin-bottom: 5px;">{{ totalTasks }}</div>
            <div style="color: #64748b; font-size: 12px;">待办任务</div>
          </div>
          <div style="text-align: center; padding: 15px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #10b981;">
            <div style="font-size: 24px; font-weight: bold; color: #10b981; margin-bottom: 5px;">{{ todayEvents }}</div>
            <div style="color: #64748b; font-size: 12px;">今日日程</div>
          </div>
          <div style="text-align: center; padding: 15px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #f59e0b;">
            <div style="font-size: 24px; font-weight: bold; color: #f59e0b; margin-bottom: 5px;">{{ recentNotes }}</div>
            <div style="color: #64748b; font-size: 12px;">本周笔记</div>
          </div>
          <div style="text-align: center; padding: 15px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #ef4444;">
            <div style="font-size: 24px; font-weight: bold; color: #ef4444; margin-bottom: 5px;">¥{{ totalExpense }}</div>
            <div style="color: #64748b; font-size: 12px;">本月支出</div>
          </div>
          <div style="text-align: center; padding: 15px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #8b5cf6;">
            <div style="font-size: 24px; font-weight: bold; color: #8b5cf6; margin-bottom: 5px;">{{ healthScore }}</div>
            <div style="color: #64748b; font-size: 12px;">健康评分</div>
          </div>
          <div style="text-align: center; padding: 15px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #06b6d4;">
            <div style="font-size: 24px; font-weight: bold; color: #06b6d4; margin-bottom: 5px;">{{ todayProgress }}%</div>
            <div style="color: #64748b; font-size: 12px;">今日进度</div>
          </div>
        </div>
      </div>

      <!-- 快速操作矩阵 -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px; margin-bottom: 20px;">
        <!-- 工作导向快捷操作 -->
        <div v-if="userMode === 'work' || userMode === 'all'" style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h3 style="color: #3b82f6; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
            💼 工作快捷操作
          </h3>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button @click="quickAddTask" style="padding: 15px; background: #3b82f620; border: 1px solid #3b82f6; border-radius: 8px; cursor: pointer; color: #3b82f6; font-weight: 500; transition: all 0.3s;" 
                    @mouseover="$event.currentTarget.style.background = '#3b82f630'" 
                    @mouseleave="$event.currentTarget.style.background = '#3b82f620'">
              📝 快速添加任务
            </button>
            <button @click="jumpToHighPriorityTasks" style="padding: 15px; background: #ef444420; border: 1px solid #ef4444; border-radius: 8px; cursor: pointer; color: #ef4444; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#ef444430'" 
                    @mouseleave="$event.currentTarget.style.background = '#ef444420'">
              🔥 高优先级任务
            </button>
            <button @click="jumpToTodayTasks" style="padding: 15px; background: #f59e0b20; border: 1px solid #f59e0b; border-radius: 8px; cursor: pointer; color: #f59e0b; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#f59e0b30'" 
                    @mouseleave="$event.currentTarget.style.background = '#f59e0b20'">
              📅 今日截止任务
            </button>
            <button @click="addMeeting" style="padding: 15px; background: #8b5cf620; border: 1px solid #8b5cf6; border-radius: 8px; cursor: pointer; color: #8b5cf6; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#8b5cf630'" 
                    @mouseleave="$event.currentTarget.style.background = '#8b5cf620'">
              📞 安排会议
            </button>
          </div>
        </div>

        <!-- 健康导向快捷操作 -->
        <div v-if="userMode === 'health' || userMode === 'all'" style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h3 style="color: #10b981; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
            🏃‍♂️ 健康快捷操作
          </h3>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button @click="quickLogExercise" style="padding: 15px; background: #10b98120; border: 1px solid #10b981; border-radius: 8px; cursor: pointer; color: #10b981; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#10b98130'" 
                    @mouseleave="$event.currentTarget.style.background = '#10b98120'">
              🏃 记录运动
            </button>
            <button @click="quickLogWeight" style="padding: 15px; background: #10b98120; border: 1px solid #10b981; border-radius: 8px; cursor: pointer; color: #10b981; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#10b98130'" 
                    @mouseleave="$event.currentTarget.style.background = '#10b98120'">
              ⚖️ 记录体重
            </button>
            <button @click="quickLogSleep" style="padding: 15px; background: #10b98120; border: 1px solid #10b981; border-radius: 8px; cursor: pointer; color: #10b981; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#10b98130'" 
                    @mouseleave="$event.currentTarget.style.background = '#10b98120'">
              😴 记录睡眠
            </button>
            <button @click="quickLogMeal" style="padding: 15px; background: #10b98120; border: 1px solid #10b981; border-radius: 8px; cursor: pointer; color: #10b981; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#10b98130'" 
                    @mouseleave="$event.currentTarget.style.background = '#10b98120'">
              🍽 记录饮食
            </button>
          </div>
        </div>

        <!-- 生活管理快捷操作 -->
        <div v-if="userMode === 'all'" style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h3 style="color: #f59e0b; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
            🏠 生活快捷操作
          </h3>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <button @click="quickAddNote" style="padding: 15px; background: #f59e0b20; border: 1px solid #f59e0b; border-radius: 8px; cursor: pointer; color: #f59e0b; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#f59e0b30'" 
                    @mouseleave="$event.currentTarget.style.background = '#f59e0b20'">
              📝 快速笔记
            </button>
            <button @click="quickRecordExpense" style="padding: 15px; background: #ef444420; border: 1px solid #ef4444; border-radius: 8px; cursor: pointer; color: #ef4444; font-weight: 500; transition: all 0.3s;"
                    @mouseover="$event.currentTarget.style.background = '#ef444430'" 
                    @mouseleave="$event.currentTarget.style.background = '#ef444420'">
              💰 记录支出
            </button>
          </div>
        </div>
      </div>

      <!-- 模块快速入口 -->
      <div style="background: white; padding: 25px; border-radius: 16px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
        <h3 style="color: #333; margin-top: 0; margin-bottom: 20px;">🎯 模块快速入口</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
          <div v-for="module in modules" :key="module.key" @click="jumpToModule(module.path)" 
               style="padding: 20px; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; border: 2px solid transparent; position: relative; overflow: hidden;"
               :style="getModuleStyle(module)"
               @mouseover="$event.currentTarget.style.transform = 'translateY(-2px)'; $event.currentTarget.style.boxShadow = '0 8px 25px rgba(0,0,0,0.15)'"
               @mouseleave="$event.currentTarget.style.transform = 'translateY(0)'; $event.currentTarget.style.boxShadow = '0 4px 16px rgba(0,0,0,0.1)'">
            <div style="display: flex; align-items: center; gap: 15px;">
              <div style="font-size: 28px;">{{ module.icon }}</div>
              <div style="flex: 1;">
                <h4 style="margin: 0 0 5px 0; color: #333;">{{ module.name }}</h4>
                <p style="margin: 0; color: #666; font-size: 14px;">{{ module.description }}</p>
                <div style="margin-top: 8px;">
                  <span style="font-size: 12px; color: #6b7280;">{{ module.stats }}</span>
                </div>
              </div>
            </div>
            <!-- 热点指示器 -->
            <div v-if="module.hot" style="position: absolute; top: 10px; right: 10px; background: #ef4444; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: bold;">
              HOT
            </div>
          </div>
        </div>
      </div>

      <!-- 今日焦点 -->
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 20px; margin-bottom: 20px;">
        <!-- 今日任务概览 -->
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h3 style="color: #333; margin-top: 0; margin-bottom: 15px;">📋 今日任务焦点</h3>
          <div v-if="todayTasks.length === 0" style="text-align: center; padding: 30px; color: #6b7280;">
            今天没有安排任务 🎉
          </div>
          <div v-else>
            <div v-for="task in todayTasks.slice(0, 5)" :key="task.id" style="padding: 12px; background: #f8fafc; border-radius: 8px; margin-bottom: 10px; display: flex; align-items: center; gap: 12px;">
              <div :style="{ width: '8px', height: '8px', borderRadius: '50%', background: getPriorityColor(task.priority) }"></div>
              <div style="flex: 1;">
                <div style="font-weight: 500; color: #333; margin-bottom: 3px;">{{ task.title }}</div>
                <div style="font-size: 12px; color: #6b7280;">{{ task.category }} | 截止: {{ task.dueDate }}</div>
              </div>
              <button @click="jumpToTaskDetail(task)" style="padding: 4px 8px; background: #667eea; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 11px;">
                查看
              </button>
            </div>
            <div v-if="todayTasks.length > 5" style="text-align: center; padding: 10px; color: #6b7280; font-size: 12px;">
              还有 {{ todayTasks.length - 5 }} 个任务...
            </div>
          </div>
        </div>

        <!-- 快速备忘录 -->
        <div style="background: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
          <h3 style="color: #333; margin-top: 0; margin-bottom: 15px;">📝 快速备忘录</h3>
          <textarea v-model="quickMemo" @input="saveQuickMemo" placeholder="在这里记录临时想法..." 
                    style="width: 100%; height: 120px; padding: 12px; border: 1px solid #e5e7eb; border-radius: 8px; resize: none; font-family: inherit;"></textarea>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
            <span style="font-size: 12px; color: #6b7280;">{{ quickMemo.length }} 字符</span>
            <div style="display: flex; gap: 8px;">
              <button @click="saveQuickMemo" style="padding: 6px 12px; background: #10b981; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 12px;">
                保存
              </button>
              <button @click="clearQuickMemo" style="padding: 6px 12px; background: #ef4444; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 12px;">
                清空
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 数据洞察 -->
      <div style="background: white; padding: 25px; border-radius: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
        <h3 style="color: #333; margin-top: 0; margin-bottom: 20px;">📊 数据洞察</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
          <div style="padding: 15px; background: #f8fafc; border-radius: 8px; border-left: 3px solid #3b82f6;">
            <h4 style="color: #3b82f6; margin: 0 0 8px 0;">任务完成率</h4>
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="flex: 1; background: #e5e7eb; height: 8px; border-radius: 4px; overflow: hidden;">
                <div :style="{ width: taskCompletionRate + '%', background: '#3b82f6', height: '100%' }"></div>
              </div>
              <span style="font-weight: bold; color: #3b82f6;">{{ taskCompletionRate }}%</span>
            </div>
          </div>
          
          <div style="padding: 15px; background: #f8fafc; border-radius: 8px; border-left: 3px solid #10b981;">
            <h4 style="color: #10b981; margin: 0 0 8px 0;">本周运动</h4>
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="font-size: 24px; font-weight: bold; color: #10b981;">{{ weeklyExercise }}</div>
              <span style="color: #6b7280;">次</span>
            </div>
          </div>
          
          <div style="padding: 15px; background: #f8fafc; border-radius: 8px; border-left: 3px solid #f59e0b;">
            <h4 style="color: #f59e0b; margin: 0 0 8px 0;">本月笔记</h4>
            <div style="display: flex; align-items: center; gap: 10px;">
              <div style="font-size: 24px; font-weight: bold; color: #f59e0b;">{{ monthlyNotes }}</div>
              <span style="color: #6b7280;">篇</span>
            </div>
          </div>
          
          <div style="padding: 15px; background: #f8fafc; border-radius: 8px; border-left: 3px solid #ef4444;">
            <h4 style="color: #ef4444; margin: 0 0 8px 0;">财务状况</h4>
            <div style="font-size: 14px; color: #6b7280;">
              本月支出: ¥{{ monthlyExpense }}<br>
              收支平衡: ¥{{ monthlyBalance }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 快速操作弹窗 -->
    <div v-if="showQuickAction" style="position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.0.7); display: flex; align-items: center; justify-content: center; z-index: 1000;">
      <div style="background: white; padding: 30px; border-radius: 16px; width: 90%; max-width: 400px;">
        <h3 style="color: #333; margin-top: 0; margin-bottom: 20px;">{{ quickActionTitle }}</h3>
        
        <div v-if="quickActionType === 'task'" style="display: grid; gap: 15px;">
          <input v-model="quickTaskTitle" placeholder="任务标题" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%;">
          <textarea v-model="quickTaskDesc" placeholder="任务描述" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%; height: 60px; resize: none;"></textarea>
          <select v-model="quickTaskPriority" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%;">
            <option value="low">低优先级</option>
            <option value="medium">中优先级</option>
            <option value="high">高优先级</option>
            <option value="urgent">紧急</option>
          </select>
        </div>
        
        <div v-if="quickActionType === 'note'" style="display: grid; gap: 15px;">
          <input v-model="quickNoteTitle" placeholder="笔记标题" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%;">
          <textarea v-model="quickNoteContent" placeholder="笔记内容" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%; height: 80px; resize: none;"></textarea>
        </div>
        
        <div v-if="quickActionType === 'expense'" style="display: grid; gap: 15px;">
          <input v-model="quickExpenseAmount" type="number" placeholder="金额" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%;">
          <input v-model="quickExpenseDesc" placeholder="消费描述" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%;">
          <select v-model="quickExpenseCategory" style="padding: 10px; border: 1px solid #d1d5db; border-radius: 6px; width: 100%;">
            <option value="餐饮">餐饮</option>
            <option value="购物">购物</option>
            <option value="交通">交通</option>
            <option value="娱乐">娱乐</option>
            <option value="其他">其他</option>
          </select>
        </div>
        
        <div style="display: flex; gap: 10px; justify-content: flex-end; margin-top: 20px;">
          <button @click="closeQuickAction" style="padding: 10px 20px; background: #ef4444; color: white; border: none; border-radius: 6px; cursor: pointer;">
            取消
          </button>
          <button @click="executeQuickAction" style="padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer;">
            执行
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userMode: 'all', // 'work', 'health', 'all'
      showQuickAction: false,
      quickActionType: '',
      quickActionTitle: '',
      quickTaskTitle: '',
      quickTaskDesc: '',
      quickTaskPriority: 'medium',
      quickNoteTitle: '',
      quickNoteContent: '',
      quickExpenseAmount: '',
      quickExpenseDesc: '',
      quickExpenseCategory: '餐饮',
      quickMemo: '',
      modules: [
        {
          key: 'tasks',
          name: '任务管理',
          icon: '📋',
          description: '管理日常任务和待办事项',
          path: '/tasks',
          stats: '4个待办',
          hot: true,
          color: '#3b82f6'
        },
        {
          key: 'calendar',
          name: '日历管理',
          icon: '📅',
          description: '查看和管理日程安排',
          path: '/calendar',
          stats: '2个今日',
          hot: false,
          color: '#10b981'
        },
        {
          key: 'knowledge',
          name: '知识库',
          icon: '📚',
          description: '记录和管理知识笔记',
          path: '/knowledge',
          stats: '15篇笔记',
          hot: false,
          color: '#f59e0b'
        },
        {
          key: 'finance',
          name: '财务管理',
          icon: '💰',
          description: '跟踪收入和支出',
          path: '/finance',
          stats: '¥2,388',
          hot: false,
          color: '#ef4444'
        },
        {
          key: 'health',
          name: '健康管理',
          icon: '🏃‍♂️',
          description: '记录健康数据和运动习惯',
          path: '/health',
          stats: '健康85分',
          hot: false,
          color: '#8b5cf6'
        },
        {
          key: 'profile',
          name: '个人设置',
          icon: '⚙️',
          description: '管理个人偏好和设置',
          path: '/profile',
          stats: '个性化',
          hot: false,
          color: '#6b7280'
        }
      ],
      // 模拟数据
      totalTasks: 4,
      todayEvents: 2,
      recentNotes: 8,
      totalExpense: '2,388',
      healthScore: 85,
      todayProgress: 65,
      todayTasks: [
        { id: 1, title: '完成项目文档', priority: 'high', category: '工作', dueDate: '12-18' },
        { id: 2, title: '团队会议', priority: 'medium', category: '工作', dueDate: '12-18' },
        { id: 3, title: '代码审查', priority: 'urgent', category: '工作', dueDate: '12-18' }
      ],
      taskCompletionRate: 75,
      weeklyExercise: 3,
      monthlyNotes: 12,
      monthlyExpense: '2,388',
      monthlyBalance: '1,612'
    }
  },
  mounted() {
    // 从本地存储恢复备忘录
    this.quickMemo = localStorage.getItem('quickMemo') || ''
    
    // 根据时间自动设置用户模式
    const hour = new Date().getHours()
    if (hour >= 9 && hour <= 17) {
      this.userMode = 'work'
    } else if (hour >= 18 || hour <= 8) {
      this.userMode = 'health'
    }
  },
  methods: {
    // 快速操作方法
    quickAddTask() {
      this.quickActionType = 'task'
      this.quickActionTitle = '快速添加任务'
      this.showQuickAction = true
    },
    quickAddNote() {
      this.quickActionType = 'note'
      this.quickActionTitle = '快速添加笔记'
      this.showQuickAction = true
    },
    quickRecordExpense() {
      this.quickActionType = 'expense'
      this.quickActionTitle = '快速记录支出'
      this.showQuickAction = true
    },
    jumpToHighPriorityTasks() {
      this.$router.push('/tasks')
      // 这里可以传递筛选参数
    },
    jumpToTodayTasks() {
      this.$router.push('/tasks')
      // 这里可以传递日期筛选
    },
    addMeeting() {
      this.$router.push('/calendar')
      // 这里可以预设会议类型
    },
    quickLogExercise() {
      this.$router.push('/health')
      // 这里可以预设运动类型
    },
    quickLogWeight() {
      this.$router.push('/health')
      // 这里可以预设体重类型
    },
    quickLogSleep() {
      this.$router.push('/health')
      // 这里可以预设睡眠类型
    },
    quickLogMeal() {
      this.$router.push('/health')
      // 这里可以预设饮食类型
    },
    jumpToModule(path) {
      this.$router.push(path)
    },
    jumpToTaskDetail(task) {
      this.$router.push('/tasks')
      // 这里可以传递任务ID
    },
    executeQuickAction() {
      if (this.quickActionType === 'task') {
        if (this.quickTaskTitle) {
          alert(`任务已添加: ${this.quickTaskTitle}`)
          // 实际项目中这里会调用API
          this.closeQuickAction()
        } else {
          alert('请输入任务标题')
        }
      } else if (this.quickActionType === 'note') {
        if (this.quickNoteTitle) {
          alert(`笔记已保存: ${this.quickNoteTitle}`)
          this.closeQuickAction()
        } else {
          alert('请输入笔记标题')
        }
      } else if (this.quickActionType === 'expense') {
        if (this.quickExpenseAmount && this.quickExpenseDesc) {
          alert(`支出已记录: ¥${this.quickExpenseAmount} - ${this.quickExpenseDesc}`)
          this.closeQuickAction()
        } else {
          alert('请输入金额和描述')
        }
      }
    },
    closeQuickAction() {
      this.showQuickAction = false
      this.quickActionType = ''
      // 清空表单
      this.quickTaskTitle = ''
      this.quickTaskDesc = ''
      this.quickTaskPriority = 'medium'
      this.quickNoteTitle = ''
      this.quickNoteContent = ''
      this.quickExpenseAmount = ''
      this.quickExpenseDesc = ''
      this.quickExpenseCategory = '餐饮'
    },
    saveQuickMemo() {
      localStorage.setItem('quickMemo', this.quickMemo)
    },
    clearQuickMemo() {
      this.quickMemo = ''
      localStorage.removeItem('quickMemo')
    },
    refreshData() {
      // 模拟数据刷新
      this.totalTasks = Math.floor(Math.random() * 10) + 1
      this.todayEvents = Math.floor(Math.random() * 5) + 1
      this.recentNotes = Math.floor(Math.random() * 20) + 5
      this.healthScore = Math.floor(Math.random() * 30) + 70
      
      alert('数据已刷新！')
    },
    getModuleStyle(module) {
      return {
        borderColor: module.color,
        background: module.color + '05'
      }
    },
    getPriorityColor(priority) {
      const colors = {
        low: '#10b981',
        medium: '#f59e0b',
        high: '#ef4444',
        urgent: '#dc2626'
      }
      return colors[priority] || '#6b7280'
    },
    backToDashboard() {
      this.$router.push('/dashboard')
    }
  }
}
</script>