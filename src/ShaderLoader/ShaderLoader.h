#pragma once
#include <stdint.h>
#include <string>

class Shader
{
public:
    // 程序ID
    uint32_t m_id;

    // 构造器读取并构建着色器
    Shader(const std::string &vertexPath, const std::string &fragmentPath);
    // 使用/激活程序
    void use();
    // uniform工具函数
    void setBool(const std::string &name, bool value) const;
    void setInt(const std::string &name, int value) const;
    void setFloat(const std::string &name, float value) const;
};