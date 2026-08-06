-- Example: governed product metric definitions
CREATE OR REPLACE VIEW analytics.product_daily_metrics AS
SELECT
    DATE(event_at) AS metric_date,
    COUNT(DISTINCT CASE
        WHEN event_name = 'session_started' THEN user_id
    END) AS dau,
    COUNT(DISTINCT CASE
        WHEN event_name = 'core_value_action' THEN user_id
    END) AS value_active_users,
    COUNT(DISTINCT CASE
        WHEN event_name = 'activation_completed' THEN user_id
    END) AS activated_users
FROM analytics.events
GROUP BY 1;
