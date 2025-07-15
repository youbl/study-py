// 主JavaScript文件
document.addEventListener('DOMContentLoaded', function() {
    // API测试功能
    const testApiBtn = document.getElementById('testApiBtn');
    const apiResult = document.getElementById('apiResult');
    
    if (testApiBtn && apiResult) {
        testApiBtn.addEventListener('click', async function() {
            testApiBtn.disabled = true;
            testApiBtn.textContent = '测试中...';
            apiResult.innerHTML = '<div class="spinner-border spinner-border-sm" role="status"></div> 正在调用API...';
            
            try {
                const response = await fetch('/api/hello');
                const data = await response.json();
                
                apiResult.innerHTML = `
                    <strong>API响应成功:</strong><br>
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                `;
                apiResult.className = 'mt-3 alert alert-success';
            } catch (error) {
                apiResult.innerHTML = `
                    <strong>API调用失败:</strong><br>
                    <span class="text-danger">${error.message}</span>
                `;
                apiResult.className = 'mt-3 alert alert-danger';
            } finally {
                testApiBtn.disabled = false;
                testApiBtn.textContent = '测试Hello API';
            }
        });
    }
    
    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // 导航栏激活状态
    const currentPath = window.location.pathname;
    document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}); 