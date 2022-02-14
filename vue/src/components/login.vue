<template>
  <div id="login">
    <div class="location">
      <el-form
        :model="ruleForm"
        status-icon
        :rules="rules"
        ref="ruleForm"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item>
          <div class="desc">C T G U 自 动 安 全 上 报</div>
        </el-form-item>

        <el-form-item label="学号" prop="user">
          <el-input v-model.number="ruleForm.user"></el-input>
        </el-form-item>

        <el-form-item label="密码" prop="password">
          <el-input
            type="password"
            v-model="ruleForm.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item label="确认密码" prop="checkpassword">
          <el-input
            type="password"
            v-model="ruleForm.checkpassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item class="submitButton">
          <el-button type="primary" @click="submitForm('ruleForm')"
            >提交</el-button
          >
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    var checkuser = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("学号不能为空"));
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error("请输入正确格式的学号"));
        } else {
          callback();
        }
      }, 1000);
    };
    var validatepassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkpassword !== "") {
          this.$refs.ruleForm.validateField("checkpassword");
        }
        callback();
      }
    };
    var validatepassword2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        password: "",
        checkpassword: "",
        user: "",
      },
      rules: {
        password: [{ validator: validatepassword, trigger: "blur" }],
        checkpassword: [{ validator: validatepassword2, trigger: "blur" }],
        user: [{ validator: checkuser, trigger: "blur" }],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.success();

          // 设置数据格式
          const headers = { "Content-Type": "multipart/form-data" };

          // 构造表单
          let data = new FormData();
          data.append("user", this.ruleForm.user);
          data.append("password", this.ruleForm.password);

          // 发请求
          this.$axios
            .post("后台数据库地址", data, {
              headers: headers,
            })
            .then(() => {
              // console.log(res)
            });

          // 提交完毕后重置表格，避免重复提交
          this.$refs[formName].resetFields();

        } else {
          this.wrong();
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
      this.$message({
        message: "注意：表格已重置",
        type: "warning",
      });
    },
    success() {
      this.$message({
        message: "提交成功",
        type: "success",
      });
    },
    wrong() {
      this.$message.error("提交失败");
    },
  },
  mounted() {
    this.$message({
      showClose: true,
      message: "注意：更改密码即可取消自动安全上报",
      type: "info",
    });
  },
};
</script>

<style lang="less">
#login {
  position: fixed;
  width: 100%;
  height: 100%;
  background: url(../assets/background.svg);
  background-size: cover;

  .location {
    background-color: rgba(0, 0, 0, 0);
    border-radius: 20px;
    width: 300px;
    height: 350px;
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    .el-form-item__label {
      text-align: left !important;
    }
  }
}
</style>
