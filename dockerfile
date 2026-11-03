
# 1. Use official Python base image
FROM python:3.12-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# 3. Set working directory
WORKDIR /app

# 4. Create a non-root application user
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

# 5. Copy dependency file
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy application code
COPY --chown=appuser:appgroup app.py .

# 8. Run as non-root user
USER appuser

# 9. Expose application port
EXPOSE 5000

# 10. Configure container health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health', timeout=2)"]

# 11. Start Flask application
CMD ["python", "app.py"]
