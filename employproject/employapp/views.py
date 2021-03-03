import random
from deap import base
from deap import creator
from deap import tools

from django.shortcuts import render ,redirect ,get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.http import require_POST
from .forms import EmployForm
from .models import EmployModel
from django.views.generic import CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
import pandas as pd


# Create your views here.
def signup_func(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        try:
           user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'signup.html',{'error':'このユーザーは既に登録されています。違う名前で登録してください。'})
    return render(request, 'signup.html',{'context':' 新規登録されました'})   

def login_func(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html',{'context':'not logged in'})
    return render(request, 'login.html',{})

@login_required
def list_func(request):
    user=request.user    
    object_list = EmployModel.objects.filter(employer=user.username)
    return render(request, 'list.html',{'object_list':object_list })

def logout_func(request):
    logout(request)
    return redirect('login')


def update_func(request, pk):
    worker = get_object_or_404(EmployModel, pk=pk)
    if request.method == "POST":
        form = EmployForm(data=request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployForm(instance=worker)
    return render(request, 'update.html', {'form': form, 'worker':worker })

class EmployCreate(CreateView):
    template_name='create.html'
    model = EmployModel
    fields = ( 'worker_name','work_day0','work_day1','work_day2','work_day3','work_day4','work_day5','work_day6',
    'work_day7', 'work_day8','work_day9','manager','employer')
    success_url = reverse_lazy('list')


@require_POST
def delete_func(request, pk):
    worker = get_object_or_404(EmployModel, pk=pk)
    worker.delete()
    return redirect('list')

def make_shift_func(request):    
    class Employee():
        def __init__(self,no,name,grade,wills):
            self.no=no
            self.name=name
            self.grade=grade
            self.wills=wills
        def is_applicated(self, box_name):
            return (box_name in self.wills)

    #ワーカーの情報定義
    user=request.user
    object_list = EmployModel.objects.filter(employer=user.username) 
    employees=[]
    
    for i in object_list:
        can_wills=[]
        if i.work_day0:
            can_wills.append('0')
        if i.work_day1:
            can_wills.append('1')
        if i.work_day2:
            can_wills.append('2')
        if i.work_day3:
            can_wills.append('3')
        if i.work_day4:
            can_wills.append('4')
        if i.work_day5:
            can_wills.append('5')
        if i.work_day6:
            can_wills.append('6')
        if i.work_day7:
            can_wills.append('7')
        if i.work_day8:
            can_wills.append('8')
        if i.work_day9:
            can_wills.append('9')
        if i.manager:
            manager = True
        else:
            manager =False
        worker = Employee(0, i.worker_name, manager, can_wills)
        employees.append(worker)
        
    

    
   

   
    class Shift():
        Shift_Box=['0','1','2','3','4','5','6','7','8','9']
        Need_People=[7,7,7,7,7,7,7,7,7,7]
        time=len(Shift_Box)
        member=len(employees)
        def __init__(self, list):
            if list == None:
                self.make_sample()
            else:
                self.list = list
                self.employees = []
      # ランダムなデータを生成
        def make_sample(self):
            sample_list = []
            for num in range(self.member*self.time):
                sample_list.append(random.randint(0, 1))
            self.list = tuple(sample_list)

      # 生成した数値(0 or 1)を1ユーザ単位に分割
        def slice(self):
            sliced = []
            start = 0
            for num in range(self.member):
                sliced.append(self.list[start:(start + self.time)])
                start +=self.time
            return tuple(sliced)
    # ユーザ別にアサインコマ名を出力する
        def print_inspect(self):
          user_no = 0
          for line in self.slice():
            print('ユーザ{}'.format(user_no))
            print (line)
            user_no +=1
            index = 0
            for e in line:
              if e == 1:
                print (self.Shift_Box[index])
                index +=1   
      # Excel形式でアサイン結果の出力をする
        def print_excel(self):
            exp_path = settings.MEDIA_ROOT + str(user.username)+'さんのシフト表.xls'
            columns_1=self.Shift_Box
            df=pd.DataFrame(columns=columns_1)
            line_data_add=[]
            employees_name=[]

            for line in self.slice():
                line_data=','.join(map(str, line))
                line_data=line_data.replace('1','〇')
                line_data=line_data.replace('0','×')
                line_data_add_pre=[]
                for n in range(0,len(line_data)+1,2):   
                    line_data_add_pre.append(line_data[n])

                line_data_add.append(line_data_add_pre)
                print (line_data)
            df2=pd.DataFrame(columns=columns_1,data=line_data_add)
            df=df.append(df2,ignore_index=True)
            for e in employees:
                employees_name.append(e.name)
            df.insert(0,'名前',employees_name)
            df.to_excel(exp_path, encoding='utf_8_sig',index=False)

    # ユーザ番号を指定してコマ名を取得する
        def get_boxes_by_user(self, user_no):
          line = self.slice()[user_no]
          return self.line_to_box(line)
        # 1ユーザ分のタプルからコマ名を取得する
        def line_to_box(self, line):
          result = []
          index = 0
          for e in line:
            if e == 1:
              result.append(self.Shift_Box[index])
            index = index + 1
          return result    
    # コマ番号を指定してアサインされているユーザ番号リストを取得する
        def get_user_nos_by_box_index(self, box_index):
          user_nos = []
          index = 0
          for line in self.slice():
            if line[box_index] == 1:
                user_nos.append(index)
            index += 1
          return user_nos
        # コマ名を指定してアサインされているユーザ番号リストを取得する
        def get_user_nos_by_box_name(self, box_name):
            box_index = self.Shift_Box.index(box_name)
            return self.get_user_nos_by_box_index(box_index)
        # 想定人数と実際の人数の差分を取得する
        def abs_people_between_need_and_actual(self):
            result = []
            index = 0
            for need in self.Need_People:
                actual = len(self.get_user_nos_by_box_index(index))
                result.append(abs(need - actual))
                index += 1
            return result
        # 希望していないコマにアサインされている件数を取得する
        def not_applicated_assign(self):
            count = 0
            for box_name in self.Shift_Box:
                user_nos = self.get_user_nos_by_box_name(box_name)
                for user_no in user_nos:
                    e = self.employees[user_no]
                    if not e.is_applicated(box_name):
                        count += 1
            return count
        #マネージャーが1人もいないコマ
        def no_senior_box(self):
            result = []
            for box_name in self.Shift_Box:
                senior_included = False
                user_nos = self.get_user_nos_by_box_name(box_name)
                for user_no in user_nos:
                  e = self.employees[user_no]
                  if e.grade:
                    senior_included = True
                if not senior_included:
                  result.append(box_name)
            return result

        #出勤の平均
        def rest_average(self):
            print('作業中')
    
    #-1000.0:いけない日に入れる、-50:先輩がいない、-100:人数が足りない(多い)
    creator.create("FitnessMax", base.Fitness, weights=(-100000.0,-50.0,-100.0))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    s =Shift([])
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, s.time*s.member)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    #目的関数
    def evalOneMax(individual):
        s=Shift(individual)
        s.employees=employees
        not_hope_count=sum(s.abs_people_between_need_and_actual())/s.member*s.time
        not_senior=len(s.no_senior_box()) /s.time
        required_people=s.not_applicated_assign() /s.member*s.time
        return not_hope_count, not_senior, required_people,


    toolbox.register("evaluate", evalOneMax)
    #交叉関数を定義(二点交叉)
    toolbox.register("mate", tools.cxTwoPoint)
    #突然変異関数を定義
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    #世代の選別
    toolbox.register("select", tools.selTournament, tournsize=3)





    # 初期集団を生成する
    pop = toolbox.population(n=300)
    CXPB, MUTPB, NGEN = 0.6, 0.5, 10 # 交差確率、突然変異確率、進化計算のループ回数
    print("進化開始")
    # 初期集団の個体を評価する
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):  # zipは複数変数の同時ループ
        # 適合性をセットする
        ind.fitness.values = fit
    print("  {} の個体を評価" .format(len(pop)))
     # 進化計算開始
    for g in range(NGEN):
        print("--{} 世代 --".format(g))
        # 選択
        # 次世代の個体群を選択
        offspring = toolbox.select(pop, len(pop))
        # 個体群のクローンを生成
        offspring = list(map(toolbox.clone, offspring))
        # 選択した個体群に交差と突然変異を適応する
        # 交叉
        # 偶数番目と奇数番目の個体を取り出して交差
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                # 交叉された個体の適合度を削除する
                del child1.fitness.values
                del child2.fitness.values
        # 変異
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # 適合度が計算されていない個体を集めて適合度を計算
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print("  {} の個体を評価" .format( len(invalid_ind)))
        # 次世代群をoffspringにする
        pop[:] = offspring
        # すべての個体の適合度を配列にする
        index = 1
        for v in ind.fitness.values:
          fits = [v for ind in pop]
          length = len(pop)
          mean = sum(fits) / length
          sum2 = sum(x*x for x in fits)
          std = abs(sum2 / length - mean**2)**0.5
          print("* パラメータ{}".format(index))
          print("  Min {}" .format( min(fits)))
          print("  Max {}".format(max(fits)))
          print("  Avg {}" .format(mean))
          print("  Std {}".format(std))
          index += 1
    print("-- 進化終了 --")
    best_ind= tools.selBest(pop,1)[0]
    print(best_ind)
    s = Shift(best_ind)
    s.print_excel()
    return render(request,'make_shift.html',{'user':user})