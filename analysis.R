library(lme4)
library(car)
library(performance)

dt <- read.csv("./result.csv")

model_1 <- lmerTest::lmer(awake_time ~ factor(day_group) + factor(Gender) + age + readiness_temperature_deviation + (1 | user), data = dt)
model_2 <- lmerTest::lmer(rem_sleep_duration ~ factor(day_group) + age + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
model_3 <- lmerTest::lmer(deep_sleep_duration ~ factor(day_group) + age + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
model_4 <- lmerTest::lmer(light_sleep_duration ~ factor(day_group) + age + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
model_5 <- lmerTest::lmer(latency ~ factor(day_group) + factor(Gender) + age + readiness_temperature_deviation + (1 | user), data = dt)
model_6 <- lmerTest::lmer(average_breath ~ factor(day_group) + factor(Gender) + age + readiness_temperature_deviation + (1 | user), data = dt)
model_7 <- lmerTest::lmer(average_heart_rate ~ factor(day_group) + factor(Gender) + age + readiness_temperature_deviation + (1 | user), data = dt)
model_8 <- lmerTest::lmer(readiness_temperature_deviation ~ factor(day_group) + (1 | user), data = dt)
model_9 <- lmerTest::lmer(average_hrv ~ factor(day_group) + factor(Gender) + age + readiness_temperature_deviation + (1 | user), data = dt)

summary(model_1)
summary(model_2)
summary(model_3)
summary(model_4)
summary(model_5)
summary(model_6)
summary(model_7)
summary(model_8)
summary(model_9)

# 各モデルのR^2に相当する指標を計算
r2_model_1 <- r2(model_1)
r2_model_2 <- r2(model_2)
r2_model_3 <- r2(model_3)
r2_model_4 <- r2(model_4)
r2_model_5 <- r2(model_5)
r2_model_6 <- r2(model_6)
r2_model_7 <- r2(model_7)
r2_model_8 <- r2(model_8)
r2_model_9 <- r2(model_9)

# VIFの計算
vif_values2 <- vif(model_9)
# VIFの結果を表示
print(vif_values2)


model__1 <- lmerTest::lmer(deep_sleep_duration ~ factor(day_group) + age + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
summary(model__1)

model__2 <- lmerTest::lmer(deep_sleep_duration ~ factor(day_group) + age + readiness_temperature_deviation + (1 | user), data = dt)
summary(model__2)

model__3 <- lmerTest::lmer(deep_sleep_duration ~ factor(day_group, levels=c("A","B")) + age + readiness_temperature_deviation + (1 | user), data = dt)
summary(model__3)

model__4 <- lmerTest::lmer(deep_sleep_duration ~ factor(day_group, levels=c("A","B")) + readiness_temperature_deviation + (1 | user), data = dt)
summary(model__4)

model__5 <- lmerTest::lmer(deep_sleep_duration ~ readiness_temperature_deviation + (1 | user), data = dt)
summary(model__5)

model__6 <- lmerTest::lmer(deep_sleep_duration ~ (1 | user), data = dt)
summary(model__6)

#AICを計算し，適したモデルを選択
AIC(model__1)
AIC(model__2)
AIC(model__3)
AIC(model__4)
AIC(model__5)
AIC(model__6)

model___1 <- lmerTest::lmer(average_hrv ~ factor(day_group) + age + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
summary(model___1)

model___2 <- lmerTest::lmer(average_hrv ~ factor(day_group, levels=c("A","B")) + age + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
summary(model___2)

model___3 <- lmerTest::lmer(average_hrv ~ factor(day_group, levels=c("A","B")) + factor(Gender) + readiness_temperature_deviation + (1 | user), data = dt)
summary(model___3)

model___4 <- lmerTest::lmer(average_hrv ~ factor(day_group, levels=c("A","B")) + readiness_temperature_deviation + (1 | user), data = dt)
summary(model___4)

model___5 <- lmerTest::lmer(average_hrv ~ readiness_temperature_deviation + (1 | user), data = dt)
summary(model___5)

model___6 <- lmerTest::lmer(average_hrv ~ (1 | user), data = dt)
summary(model___6)

#AICを計算し，適したモデルを選択
AIC(model___1)
AIC(model___2)
AIC(model___3)
AIC(model___4)
AIC(model___5)
AIC(model___6)

#選択されたモデルのR2を計算
r2_model__3 <- r2(model__3)
r2_model___2 <- r2(model___2)
print(r2_model__3)
print(r2_model___2)
